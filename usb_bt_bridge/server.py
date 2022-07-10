# -*- coding: utf-8 -*-
from pathlib import Path
import configparser
import dbus
import dbus.service
import gi
import os
import subprocess
import sys
import time
import logging
from bluetooth import BluetoothSocket, L2CAP
from struct import pack

from .constants import *

log = logging.getLogger(__name__)

# sleep time after Bluetooth command line tools
BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
AGENT_PATH = "/test/agent"
DBUS_OM_IFACE = "org.freedesktop.DBus.ObjectManager"
DBUS_PROP_IFACE = "org.freedesktop.DBus.Properties"

GATT_SERVICE_IFACE = "org.bluez.GattService1"
GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
GATT_DESC_IFACE = "org.bluez.GattDescriptor1"

LE_ADVERTISING_MANAGER_IFACE = "org.bluez.LEAdvertisingManager1"
LE_ADVERTISEMENT_IFACE = "org.bluez.LEAdvertisement1"

BLUEZ_SERVICE_NAME = "org.bluez"
GATT_MANAGER_IFACE = "org.bluez.GattManager1"


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report)#.encode())


def find_adapter(bus):
    """
    Returns the first object that the bluez service has that has a GattManager1 interface
    """
    remote_om = dbus.Interface(bus.get_object(BLUEZ_SERVICE_NAME, "/"), DBUS_OM_IFACE)
    objects = remote_om.GetManagedObjects()

    for o, props in objects.items():
        if GATT_MANAGER_IFACE in props.keys():
            return o

    return None


class BTKbdBluezProfile(dbus.service.Object):
    """Bluez 5 profile for emulated Bluetooth Keyboard"""
    fd = -1

    def __init__(self, bus, path, mainloop):
        dbus.service.Object.__init__(self, bus, path)
        self.mainloop = mainloop

    @dbus.service.method("org.bluez.Profile1", in_signature="",
                         out_signature="")
    def Release(self):
        log.info("[*] Release")
        self.mainloop.quit()

    @dbus.service.method("org.bluez.Profile1",
                         in_signature="", out_signature="")
    def Cancel(self):
        log.info("[*] Cancel")

    @dbus.service.method("org.bluez.Profile1", in_signature="oha{sv}",
                         out_signature="")
    def NewConnection(self, path, fd, properties):
        self.fd = fd.take()
        log.info("[*] NewConnection({}, {:d})".format(path, self.fd))
        for key in properties.keys():
            if key == "Version" or key == "Features":
                log.info("    {} = 0x{:04x}".format(key, properties[key]))
            else:
                log.info("    {} = {}".format(key, properties[key]))

    @dbus.service.method("org.bluez.Profile1", in_signature="o",
                         out_signature="")
    def RequestDisconnection(self, path):
        log.info("[*] RequestDisconnection({})".format(path))

        if (self.fd > 0):
            os.close(self.fd)
            self.fd = -1


def read_sdp_service_record(path):
    """Read SDP service record"""

    log.info("[*] Reading service record")
    try:
        fh = open(path, "r")
    except Exception:
        sys.exit("[*] Could not open the SDP record. Exiting ...")

    return fh.read()


def power_on(bus):
    adapter = find_adapter(bus)
    log.info(adapter)
    adapter_obj = bus.get_object(BUS_NAME, adapter)
    adapter_props = dbus.Interface(adapter_obj, "org.freedesktop.DBus.Properties")
    adapter_props.Set("org.bluez.Adapter1", "Powered", dbus.Boolean(1))


def discoverable_on(bus):
    adapter = find_adapter(bus)
    log.info(adapter)
    adapter_obj = bus.get_object(BUS_NAME, adapter)
    adapter_props = dbus.Interface(adapter_obj, "org.freedesktop.DBus.Properties")
    adapter_props.Set("org.bluez.Adapter1", "Discoverable", dbus.Boolean(1))


def register_bluez_profile(bus, path, device_uuid):
    """Setup and register BlueZ profile"""

    log.info("Configuring Bluez Profile")
    # file path of the SDP record
    filename = 'sdp2.xml'
    # filename = 'sdp_record.xml'
    filename = 'sdp3.xml'
    sdp_path = os.path.join(Path(__file__).parent.absolute(), filename)
    # setup profile options
    service_record = read_sdp_service_record(sdp_path)
    # descriptor = KEYBOARD_DESCRIPTOR
    descriptor = DESCRIPTOR_3
    descriptor = "".join(["%02X" % x for x in descriptor])
    # log.info(descriptor)
    service_record = service_record.replace("SERVICE_DESCRIPTOR", descriptor)
    # log.info(service_record)
    opts = {
            # "AutoConnect": True,
            "ServiceRecord": service_record.replace("SERVICE_DESCRIPTOR", descriptor),
            "Role": "server",
            "RequireAuthentication": False,
            "RequireAuthorization": False
            }


    # retrieve a proxy for the bluez profile interface
    manager = dbus.Interface(bus.get_object("org.bluez", "/org/bluez"), "org.bluez.ProfileManager1")
    # unregister if possible

    try:
        manager.UnregisterProfile(path)
    except dbus.DBusException as e:
        log.error(e)

    # log.info(path, device_uuid, opts)
    manager.RegisterProfile(path, device_uuid, opts)

    log.info("[*] Profile registered")


class BTKbDevice():
    """Bluetooth HID keyboard device"""

    # control and interrupt service ports
    P_CTRL = 17                     # Service port (control) from SDP record
    P_INTR = 19                     # Service port (interrupt) from SDP record

    # D-Bus path of the BlueZ profile

    def __init__(self, addr):
        """Initialize Bluetooth keyboard device"""

        self.auto_connect = False
        self.bdaddr = addr
        self.connections = {}
        self.connection_count = 0

    def listen(self):
        """Listen for incoming client connections"""

        log.info("[*] Waiting for connections on %s", self.bdaddr)
        self.scontrol = BluetoothSocket(L2CAP)
        self.sinterrupt = BluetoothSocket(L2CAP)

        # bind these sockets to a port - port zero to select next available
        self.scontrol.bind((self.bdaddr, self.P_CTRL))
        self.sinterrupt.bind((self.bdaddr, self.P_INTR))

        # start listening on the server sockets (only allow 1 connection)
        self.scontrol.listen(1)
        self.sinterrupt.listen(1)

        ccontrol, cinfo = self.scontrol.accept()
        log.info("[*] Connection on the control channel from {}"
              .format(cinfo[0]))

        cinterrupt, cinfo = self.sinterrupt.accept()
        log.info("[*] Connection on the interrupt channel from {}"
              .format(cinfo[0]))

        self.add_connection(ccontrol, cinterrupt)

        log.info("Listen exit")

    def connect(self, target):
        """Connect to target MAC (the keyboard must already be known to the
        target)"""

        log.info("[*] Connecting to {}".format(target))
        scontrol = BluetoothSocket(L2CAP)
        sinterrupt = BluetoothSocket(L2CAP)

        scontrol.connect((target, self.P_CTRL))
        sinterrupt.connect((target, self.P_INTR))

        self.add_connection(scontrol, sinterrupt)

    def add_connection(self, control, interrupt):
        self.connection_count += 1
        self.connections[self.connection_count] = (control, interrupt)

    def send_string(self, message):
        """Send a string to the host machine"""

        log.info("M: %s", str(message[2:]))
        write_report(message[2:])
        
        if len(self.connections) == 0:
            log.info("Not connected")
            return

        reap_connection = []

        for k, v in self.connections.items():
            try:
                v[1].send(message)
            except:
                reap_connection.append(k)
                import traceback
                traceback.print_exc()

        for k in reap_connection:
            self.connections.pop(k, None)


class BTKbdService:
    """D-Bus service for emulated Bluetooth keyboard"""

    def __init__(self, device):
        log.info("[*] Inititalize D-Bus Bluetooth keyboard service")
        self.device = device

    def listen(self):
        try:
            while True:
                self.device.listen()
        except KeyboardInterrupt:
            log.info("Interrupt")

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

    def send_mouse(self, buttons, x, y, w):
        byte_list = [0xA1, 0x02, buttons & 0x1f, x, y, w]
        log.info('send %s', byte_list)
        data = pack("3B3b", *byte_list)
        self.device.send_string(data)

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

        log.info('send %s', byte_list)

        data = pack("10B", *byte_list)

        self.device.send_string(data)


