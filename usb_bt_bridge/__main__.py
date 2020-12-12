import time
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')
import os, sys
from .client import Keyboard
import threading
from .server import BTKbdService
from dbus.mainloop.glib import DBusGMainLoop
import dbus.mainloop.glib
from .usbdevices import main as usbdevices_main
import logging

# Main eventloop import
try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(thread)s %(name)s %(message)s')
    print('start')

    # check for required root privileges
    if not os.geteuid() == 0:
        sys.exit("[-] Please run the keyboard server as root")
    mainloop = GObject.MainLoop()

    # start D-Bus Bluetooth keyboard emulator service
    DBusGMainLoop(set_as_default=True)
    addr = '14:F6:D8:B5:09:86'
    # you should probably have addr be empty. so it binds on the default iface
    addr = ''
    # addr = "00:01:02:03:04:06"
    btkbdservice = BTKbdService(addr)
    kbd = Keyboard(btkbdservice)

    config_filename = sys.argv[1]
    threading.Thread(target=lambda: usbdevices_main(kbd, config_filename)).start()
    threading.Thread(target=lambda: kbd.event_loop()).start()
    threading.Thread(target=btkbdservice.listen).start()
    try:
        print('loop')
        mainloop.run()
    except KeyboardInterrupt:
        print('Interrupt')
        pass

    # b = threading.Thread(target=Gtk.main).start()
    # a.join()

