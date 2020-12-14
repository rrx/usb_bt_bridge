#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Bluetooth Keyboard Emulator D-Bus Agent

  Based on the BlueZ simple-agent

  http://www.bluez.org/
"""

import dbus
import dbus.service
import dbus.mainloop.glib

import time
import traceback

# from gi.repository import GObject
from gi.repository import GLib
from optparse import OptionParser
import logging


log = logging.getLogger(__name__)

BUS_NAME = 'org.bluez'
AGENT_INTERFACE = 'org.bluez.Agent1'
AGENT_PATH = "/test/agent"

device_obj = None
dev_path = None


def ask(prompt):
    try:
        return raw_input(prompt)
    except:
        return input(prompt)


def set_trusted(path):
    bus = dbus.SystemBus()
    props = dbus.Interface(bus.get_object("org.bluez", path),
            "org.freedesktop.DBus.Properties")
    props.Set("org.bluez.Device1", "Trusted", True)
    log.info('trusted %s', path)

def dev_connect(path):
    dev = dbus.Interface(bus.get_object("org.bluez", path),
            "org.bluez.Device1")
    dev.Connect()


class Rejected(dbus.DBusException):
    _dbus_error_name = "org.bluez.Error.Rejected"


class Agent(dbus.service.Object):
    exit_on_release = True

    def __init__(self, bus, path, mainloop):
        dbus.service.Object.__init__(self, bus, path)
        self.loop = mainloop

    def set_exit_on_release(self, exit_on_release):
            self.exit_on_release = exit_on_release

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Release(self):
        log.info("Release")
        if self.exit_on_release:
            self.loop.quit()

    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def AuthorizeService(self, device, uuid):
        log.info("AuthorizeService ({}, {})".format(device, uuid))
        authorize = ask("Authorize connection (yes/no): ")
        if (authorize == "yes"):
            return
        raise Rejected("Connection rejected by user")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="s")
    def RequestPinCode(self, device):
        log.info("RequestPinCode ({})".format(device))
        set_trusted(device)
        return ask("Enter PIN Code: ")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="u")
    def RequestPasskey(self, device):
        log.info("RequestPasskey ({})".format(device))
        set_trusted(device)
        passkey = ask("Enter passkey: ")
        return dbus.UInt32(passkey)

    @dbus.service.method(AGENT_INTERFACE, in_signature="ouq", out_signature="")
    def DisplayPasskey(self, device, passkey, entered):
        log.info("DisplayPasskey ({}, {:06u} entered {:u})".
              format(device, passkey, entered))

    @dbus.service.method(AGENT_INTERFACE, in_signature="os", out_signature="")
    def DisplayPinCode(self, device, pincode):
        log.info("DisplayPinCode ({}, {})".format(device, pincode))

    @dbus.service.method(AGENT_INTERFACE, in_signature="ou", out_signature="")
    def RequestConfirmation(self, device, passkey):
        log.info("RequestConfirmation ({}, {:06d}".format(device, passkey))
        # confirm = ask("Confirm passkey (yes/no): ")
        set_trusted(device)
        return

        if (confirm == "yes"):
            set_trusted(device)
            return
        raise Rejected("Passkey doesn't match")

    @dbus.service.method(AGENT_INTERFACE, in_signature="o", out_signature="")
    def RequestAuthorization(self, device):
        log.info("RequestAuthorization ({})".format(device))
        auth = ask("Authorize? (yes/no): ")
        if (auth == "yes"):
            return
        raise Rejected("Pairing rejected")

    @dbus.service.method(AGENT_INTERFACE, in_signature="", out_signature="")
    def Cancel(self):
        log.info("Cancel")


def pair_reply():
    log.info("Device paired")
    set_trusted(dev_path)
    dev_connect(dev_path)


def pair_error(error):
    err_name = error.get_dbus_name()
    if err_name == "org.freedesktop.DBus.Error.NoReply" and device_obj:
        log.info("Timed out. Cancelling pairing")
        device_obj.CancelPairing()
    else:
        log.info("Creating device failed: {}".format(error))


def register_agent(bus, path):
    obj = bus.get_object(BUS_NAME, "/org/bluez")
    manager = dbus.Interface(obj, "org.bluez.AgentManager1")
    try:
        manager.UnregisterAgent(path)
    except dbus.DBusException as e:
        log.error(e)

    capability = "KeyboardDisplay"
    manager.RegisterAgent(path, capability)

    log.info("[*] Agent registered")
    manager.RequestDefaultAgent(path)


def event_loop(mainloop, bus, path):
    agent = Agent(bus, path, mainloop)

    while True:
        try:
            register_agent(bus, path)
            mainloop.run()
            log.info("loop exit, restarting")
        except KeyboardInterrupt:
            log.info("Agent Interrupt")
            break
        except:
            traceback.print_exc()

        log.info("restart")
        time.sleep(1)

    log.info("Agent Exit")


def main():
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    dbus.mainloop.glib.threads_init()
    mainloop = GLib.MainLoop()
    bus = dbus.SystemBus()
    path = "/test/agent"
    event_loop(mainloop, bus, path)


if __name__ == '__main__':
    main()


