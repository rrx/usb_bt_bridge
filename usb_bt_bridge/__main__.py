import time
from gi.repository import GLib
import gi
import os, sys
import threading
from dbus.mainloop.glib import DBusGMainLoop
import dbus.mainloop.glib
import logging
import traceback

from .client import Keyboard
from .server import BTKbdService, BTKbdBluezProfile, register_bluez_profile, power_on, discoverable_on, BTKbDevice
from .usbdevices import main as usbdevices_main
from .agent import event_loop as agent_event_loop, register_agent, Agent

PROFILE_DBUS_PATH = "/test/bridge_profile"
# device UUID
UUID = "00001124-0000-1000-8000-00805f9b34fb"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(thread)s %(name)s %(message)s')
    log = logging.getLogger(__name__)

    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    dbus.mainloop.glib.threads_init()
    mainloop = GLib.MainLoop()
    bus = dbus.SystemBus()
    agent_path = '/test/agent'

    # check for required root privileges
    if not os.geteuid() == 0:
        sys.exit("[-] Please run the keyboard server as root")

    # addr = '14:F6:D8:B5:09:86'
    # you should probably have addr be empty. so it binds on the default iface
    addr = ''
    # addr = "00:01:02:03:04:06"

    power_on(bus)
    discoverable_on(bus)

    # create agent service
    agent = Agent(bus, agent_path, mainloop)
    profile = BTKbdBluezProfile(bus, PROFILE_DBUS_PATH, mainloop)
    device = BTKbDevice(addr)
    btkbdservice = BTKbdService(device)
    kbd = Keyboard(btkbdservice)

    def loop():
        while True:
            try:
                register_agent(bus, agent_path)
                register_bluez_profile(bus, PROFILE_DBUS_PATH, UUID)
                mainloop.run()
                log.info("loop exit, restarting")
            except KeyboardInterrupt:
                log.error("Main Interrupt")
                break
            except:
                traceback.print_exc()

            log.info("restart")
            time.sleep(1)

        log.info("Main Exit")

    config_filename = sys.argv[1]
    ts = [
        threading.Thread(target=lambda: usbdevices_main(kbd, config_filename)),
        threading.Thread(target=kbd.event_loop),
        threading.Thread(target=btkbdservice.listen),
        threading.Thread(target=loop)
    ]

    # start threads
    [t.start() for t in ts]

