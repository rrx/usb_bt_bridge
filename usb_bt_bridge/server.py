#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Bluetooth Keyboard Emulator D-Bus Server

  by Matthias Deeg <matthias.deeg@syss.de>, SySS GmbH

  based on BlueZ 5 Bluetooth Keyboard Emulator for Raspberry Pi
  (YAPTB Bluetooth keyboard emulator) by Thanh Le
  Source code and information of this project can be found via
  https://github.com/0xmemphre/BL_keyboard_RPI,
  http://www.mlabviet.com/2017/09/make-raspberry-pi3-as-emulator.html

  MIT License

  Copyright (c) 2018 SySS GmbH
  Copyright (c) 2017 quangthanh010290

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
"""

__version__ = '1.0'
__author__ = 'Matthias Deeg'

from pathlib import Path
import configparser
import dbus
import dbus.service
import dbus.mainloop
import dbus.mainloop.glib
import gi
import os
import subprocess
import sys
import time

from bluetooth import BluetoothSocket, L2CAP
from struct import pack
# from .agent import Agent

# sleep time after Bluetooth command line tools
OS_CMD_SLEEP = 1.5
BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
AGENT_PATH = "/test/agent"


def ask(prompt):
    try:
        return raw_input(prompt)
    except:
        return input(prompt)


class Rejected(dbus.DBusException):
    _dbus_error_name = "org.bluez.Error.Rejected"


def set_trusted(path):
    print('set_trusted', path)
    bus = dbus.SystemBus()
    # bus = self.device.bus
    props = dbus.Interface(bus.get_object("org.bluez", path),
            "org.freedesktop.DBus.Properties")
    props.Set("org.bluez.Device1", "Trusted", True)
    print('trusted')


class Agent(dbus.service.Object):
    def __init__(self, bus, path, device=None):
        dbus.service.Object.__init__(self, bus, path)
        self.device = device


    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Release(self):
        print("Release")

    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        print("AuthorizeService ({}, {})".format(device, uuid))
        authorize = ask("Authorize connection (yes/no): ")
        if (authorize == "yes"):
            return
        raise Rejected("Connection rejected by user")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        print("RequestPinCode ({})".format(device))
        set_trusted(device)
        return ask("Enter PIN Code: ")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        print("RequestPasskey ({})".format(device))
        set_trusted(device)
        passkey = ask("Enter passkey: ")
        return dbus.UInt32(passkey)

    @dbus.service.method(AGENT_INTERFACE, in_signature="ouq", out_signature="")
    def DisplayPasskey(self, device, passkey, entered):
        print("DisplayPasskey ({}, {:06u} entered {:u})".
              format(device, passkey, entered))

    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def DisplayPinCode(self, device, pincode):
        print("DisplayPinCode ({}, {})".format(device, pincode))

    @dbus.service.method(AGENT_INTERFACE, in_signature="ou", out_signature="")
    def RequestConfirmation(self, path, passkey):
        print("RequestConfirmation ({}, {:06d})".format(path, passkey))
        set_trusted(path)
        # TODO: implement something better here
        # confirm = ask("Confirm passkey (yes/no): ")
        # if (confirm == "yes"):
            # set_trusted(path)
            # return
        # raise Rejected("Passkey doesn't match")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        print("RequestAuthorization ({})".format(device))
        auth = ask("Authorize? (yes/no): ")
        if (auth == "yes"):
            return
        raise Rejected("Pairing rejected")

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        print("Cancel")




class BTKbdBluezProfile(dbus.service.Object):
    """Bluez 5 profile for emulated Bluetooth Keyboard"""
    fd = -1

    def __init__(self, bus, path):
        dbus.service.Object.__init__(self, bus, path)

    @dbus.service.method("org.bluez.Profile1", in_signature="",
                         out_signature="")
    def Release(self):
        print("[*] Release")
        dbus.mainloop.quit()

    @dbus.service.method("org.bluez.Profile1",
                         in_signature="", out_signature="")
    def Cancel(self):
        print("[*] Cancel")

    @dbus.service.method("org.bluez.Profile1", in_signature="oha{sv}",
                         out_signature="")
    def NewConnection(self, path, fd, properties):
        self.fd = fd.take()
        print("[*] NewConnection({}, {:d})".format(path, self.fd))
        for key in properties.keys():
            if key == "Version" or key == "Features":
                print("    {} = 0x{:04x}".format(key, properties[key]))
            else:
                print("    {} = {}".format(key, properties[key]))

    @dbus.service.method("org.bluez.Profile1", in_signature="o",
                         out_signature="")
    def RequestDisconnection(self, path):
        print("[*] RequestDisconnection({})".format(path))

        if (self.fd > 0):
            os.close(self.fd)
            self.fd = -1


class BTKbDevice():
    """Bluetooth HID keyboard device"""

    # control and interrupt service ports
    P_CTRL = 17                     # Service port (control) from SDP record
    P_INTR = 19                     # Service port (interrupt) from SDP record

    # D-Bus path of the BlueZ profile
    PROFILE_DBUS_PATH = "/bluez/syss/btkbd_profile"

    # file path of the SDP record
    filename = 'sdp2.xml'
    # SDP_RECORD_PATH = os.path.join(Path(__file__).parent.absolute(), "sdp_record.xml")
    SDP_RECORD_PATH = os.path.join(Path(__file__).parent.absolute(), filename)
    print(SDP_RECORD_PATH)

    # device UUID
    UUID = "00001124-0000-1000-8000-00805f9b34fb"

    def __init__(self, addr):
        """Initialize Bluetooth keyboard device"""

        self.auto_connect = False
        self.bdaddr = addr
        self.bus = dbus.SystemBus()

        print("[*] Initialize Bluetooth device")
        self.register_bluez_profile()
        self.register_agent()

    def register_agent(self):
        capability = "KeyboardDisplay"
        path = "/test/agent"
        agent = Agent(self.bus, path, device=self)
        obj = self.bus.get_object(BUS_NAME, "/org/bluez")
        manager = dbus.Interface(obj, "org.bluez.AgentManager1")
        manager.RegisterAgent(path, capability)
        manager.RequestDefaultAgent(path)
        print("[*] Agent registered")

    def register_bluez_profile(self):
        """Setup and register BlueZ profile"""

        print("Configuring Bluez Profile")

        # setup profile options
        service_record = self.read_sdp_service_record()

        opts = {
                "AutoConnect": True,
                "ServiceRecord": service_record,
                # "Role": "server",
                # "RequireAuthentication": False,
                # "RequireAuthorization": False
                }

        # retrieve a proxy for the bluez profile interface
        bus = dbus.SystemBus()
        manager = dbus.Interface(bus.get_object("org.bluez", "/org/bluez"),
                                 "org.bluez.ProfileManager1")

        profile = BTKbdBluezProfile(bus, BTKbDevice.PROFILE_DBUS_PATH)

        manager.RegisterProfile(BTKbDevice.PROFILE_DBUS_PATH, BTKbDevice.UUID,
                                opts)

        print("[*] Profile registered")

    def read_sdp_service_record(self):
        """Read SDP service record"""

        print("[*] Reading service record")
        try:
            fh = open(BTKbDevice.SDP_RECORD_PATH, "r")
        except Exception:
            sys.exit("[*] Could not open the SDP record. Exiting ...")

        return fh.read()

    def listen(self):
        """Listen for incoming client connections"""

        print("[*] Waiting for connections on", self.bdaddr)
        self.scontrol = BluetoothSocket(L2CAP)
        self.sinterrupt = BluetoothSocket(L2CAP)

        # bind these sockets to a port - port zero to select next available
        self.scontrol.bind((self.bdaddr, self.P_CTRL))
        self.sinterrupt.bind((self.bdaddr, self.P_INTR))

        # start listening on the server sockets (only allow 1 connection)
        self.scontrol.listen(1)
        self.sinterrupt.listen(1)

        self.ccontrol, cinfo = self.scontrol.accept()
        print("[*] Connection on the control channel from {}"
              .format(cinfo[0]))

        self.cinterrupt, cinfo = self.sinterrupt.accept()
        print("[*] Connection on the interrupt channel from {}"
              .format(cinfo[0]))

    def connect(self, target):
        """Connect to target MAC (the keyboard must already be known to the
        target)"""

        print("[*] Connecting to {}".format(target))
        self.scontrol = BluetoothSocket(L2CAP)
        self.sinterrupt = BluetoothSocket(L2CAP)

        self.scontrol.connect((target, self.P_CTRL))
        self.sinterrupt.connect((target, self.P_INTR))

        self.ccontrol = self.scontrol
        self.cinterrupt = self.sinterrupt

    def send_string(self, message):
        """Send a string to the host machine"""

        try:
            self.cinterrupt.send(message)
        except:
            import traceback
            traceback.print_exc()


class BTKbdService:
    """D-Bus service for emulated Bluetooth keyboard"""

    def __init__(self, addr):
        print("[*] Inititalize D-Bus Bluetooth keyboard service")

        # create and setup our device
        self.device = BTKbDevice(addr)

    def listen(self):
        self.device.listen()

        # if self.device.auto_connect == "true":
            # # Switch into paring mode or connect to already known target?
            # # files = os.listdir('/var/lib/bluetooth/{}'.format(self.device.bdaddr))
            # # mac_regex = re.compile(r'([0-9A-F]{2}:){5}([0-9A-F]{2})')
            # # files = list(filter(mac_regex.match, files))
            # # if files:
            # # connect to configured target
            # self.device.connect(self.device.connect_target)
        # else:
            # # start listening for new connections
            # self.device.listen()

    def send_keys(self, modifiers, keys):
        """Send keys"""

        # create 10 byte data structure
        byte_list = [0xA1, 0x01, modifiers, 0x00]
        for key_code in keys:
            byte_list.append(key_code)

        # add some padding bytes to have a 10 byte packet
        if len(byte_list) < 10:
            padding = len(byte_list) - 10
            for i in range(padding):
                byte_list.append(0)

        data = pack("10B", *byte_list)

        self.device.send_string(data)


