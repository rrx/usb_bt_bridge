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
    # GObject.threads_init()
    # dbus.mainloop.glib.threads_init()
    # Gtk.threads_init()
    # check for required root privileges
    if not os.geteuid() == 0:
        sys.exit("[-] Please run the keyboard server as root")

    # start D-Bus Bluetooth keyboard emulator service
    DBusGMainLoop(set_as_default=True)
    btkbdservice = BTKbdService("00:01:02:03:04:06")
    kbd = Keyboard(btkbdservice)
    threading.Thread(target=lambda: usbdevices_main(sys.argv[1])).start()
    threading.Thread(target=lambda: kbd.event_loop('/dev/input/event8')).start()
    threading.Thread(target=btkbdservice.listen).start()
    # btkbdservice.listen()
    # kbd.event_loop('/dev/input/event8')
    print('loop')
    mainloop = GObject.MainLoop()
    mainloop.run()

    # b = threading.Thread(target=Gtk.main).start()
    # a.join()

