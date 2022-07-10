# -*- coding: utf-8 -*-
"""
https://source.android.com/devices/input/keyboard-devices.html
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2

"""
import logging
log = logging.getLogger(__name__)

import dbus
import dbus.service
from .constants import KEY_RECORDS
import evdev
from evdev import InputDevice, ecodes
from evdev.events import event_factory
from selectors import DefaultSelector, EVENT_READ
import selectors

import sys

LOOKUP = dict([(key, code) for key, code, _ in KEY_RECORDS] + [(code, key) for key, code, _ in KEY_RECORDS])

# USB HID keyboard modifier
MODIFIER_NONE           = 0
MODIFIER_CONTROL_LEFT   = 1 << 0
MODIFIER_SHIFT_LEFT     = 1 << 1
MODIFIER_ALT_LEFT       = 1 << 2
MODIFIER_GUI_LEFT       = 1 << 3
MODIFIER_CONTROL_RIGHT  = 1 << 4
MODIFIER_SHIFT_RIGHT    = 1 << 5
MODIFIER_ALT_RIGHT      = 1 << 6
MODIFIER_GUI_RIGHT      = 1 << 7

# USB HID key codes
KEY_NONE                = 0x00

class Keyboard:
    """Emulated keyboard"""

    def __init__(self, service):
        # state structure of the emulated Bluetooth keyboard
        self.state = [
            0xA1,       # input report
            0x01,       # usage report : keyboard
            0x00,       # modifier byte
            0x00,       # Vendor reserved
            0x00,       # 6 bytes for key codes
            0x00,
            0x00,
            0x00,
            0x00,
            0x00]

        self.mouse_buttons = 0

        self.service = service
        self.pressed_key_count = 0              # initialize keypress counter
        self.selector = DefaultSelector()

    def device_add(self, args, device):
        try:
            dev = InputDevice(device.device_node)
            log.info(dev)
            self.selector.register(dev, selectors.EVENT_READ)
        except:# RuntimeException as e:
            import traceback
            traceback.print_exc()

    def device_remove(self, args, device):
        try:
            dev = InputDevice(device.device_node)
            self.selector.unregister(dev)
        except:
            import traceback
            traceback.print_exc()

    def change_state(self, keydata, keypress=True):
        """Change keyboard state"""

        log.info("key count {}".format(self.pressed_key_count))

        if keypress:
            if keydata[0] != MODIFIER_NONE and keydata[1] != KEY_NONE:
                if keydata[1] not in self.state[4:]:
                    # increase key count
                    self.pressed_key_count += 1

                    # find free key slot
                    i = self.state[4:].index(0)

                    # set key
                    self.state[4 + i] = keydata[1]
                    log.info("Key press {}".format(keydata[1]))

                self.state[2] = keydata[0]


            elif keydata[1] != KEY_NONE:
                if keydata[1] not in self.state[4:]:
                    # increase key count
                    self.pressed_key_count += 1

                    # find free key slot
                    i = self.state[4:].index(0)

                    # set key
                    self.state[4 + i] = keydata[1]
                    log.info("Key press {}".format(keydata[1]))

            elif keydata[0] != MODIFIER_NONE and keydata[1] == KEY_NONE:
                # process modifier keys
                log.info("{} pressed".format(keydata[0]))

                self.state[2] |= keydata[0]
                log.info("Modify modifier byte {}".format(self.state[2]))

            elif keydata[2] != 0:
                self.mouse_buttons |= keydata[2]
                self.service.send_mouse(self.mouse_buttons, 0, 0, 0)
                return

        else:
            if keydata[1] != KEY_NONE:
                # decrease keypress count
                self.pressed_key_count -= 1
                log.info("Key release {}".format(keydata[1]))

                # update state
                i = self.state[4:].index(keydata[1])
                self.state[4 + i] = 0

            if keydata[0] != MODIFIER_NONE:
                log.info("{} released".format(keydata[0]))
                self.state[2] &= ~keydata[0]

            elif keydata[2] != 0:
                self.mouse_buttons &= ~keydata[2]
                self.service.send_mouse(self.mouse_buttons, 0, 0, 0)
                return


        modifier_byte = self.state[2]
        self.service.send_keys(modifier_byte, self.state[4:10])

    def on_press(self, k):
        """Change keyboard state on key presses"""
        if self.pressed_key_count < 7:
            # set state of newly pressed key but consider limit of max. 6 keys
            # pressed at the same time
            self.change_state(k)

    def on_release(self, k):
        """Change keyboard state on key releases"""
        # change keyboard state
        self.change_state(k, False)

    def on_move(self, x, y, w):
        self.service.send_mouse(0, x, y, w)

    def event_loop(self):
        try:
            while True:
                for key, mask in self.selector.select():
                    device = key.fileobj
                    for event in device.read():
                        if event.type == ecodes.EV_KEY:
                            # print('E', event.type, event.value, event.code, "0x%02x" % event.code)
                            ce = evdev.util.categorize(event)
                            # print(ce.scancode, ce.keystate, ce.keycode)

                            key = key_from_event(ce)
                            if event.value == 0:
                                self.on_release(key)
                            elif event.value == 1:
                                self.on_press(key)
                        elif event.type == ecodes.EV_REL:
                            # print('E', event.type, event.value, event.code, "0x%02x" % event.code)
                            if event.code == 0:
                                # rel_x
                                self.on_move(event.value, 0, 0)
                            elif event.code == 1:
                                # rel_y
                                self.on_move(0,event.value,0)
                            elif event.code == 8:
                                # vwheel
                                self.on_move(0,0,event.value)

                        else:
                            log.debug("Unhandled %s", event)

        except KeyboardInterrupt:
            pass

    def __str__(self):
        """Keyboard state as string"""

        return repr(self.state)

modifier_mapping = {
    'KEY_LEFTSHIFT': MODIFIER_SHIFT_LEFT,
    'KEY_RIGHTSHIFT': MODIFIER_SHIFT_RIGHT,
    'KEY_LEFTCTRL': MODIFIER_CONTROL_LEFT,
    'KEY_RIGHTCTRL': MODIFIER_CONTROL_RIGHT,
    'KEY_LEFTALT': MODIFIER_ALT_LEFT,
    'KEY_RIGHTALT': MODIFIER_ALT_RIGHT,
    'KEY_LEFTMETA': MODIFIER_GUI_LEFT,
    'KEY_RIGHTMETA': MODIFIER_GUI_RIGHT,
}

mouse_mapping = {
    'BTN_LEFT': 1,
    'BTN_RIGHT': 2,
    'BTN_MIDDLE': 4,
}

def key_from_event(e):
    k = e.keycode

    if isinstance(k, list):
        k = k[0]

    if k in modifier_mapping:
        return [LOOKUP[k], KEY_NONE, 0]

    v = LOOKUP.get(k)
    if v:
        return [MODIFIER_NONE, v, 0]

    v = mouse_mapping.get(k)
    if v:
        return [MODIFIER_NONE, KEY_NONE, v]

    log.debug("*** Missing %s", e)
    return [MODIFIER_NONE, KEY_NONE, 0]

