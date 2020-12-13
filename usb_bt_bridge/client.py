# -*- coding: utf-8 -*-
"""
https://source.android.com/devices/input/keyboard-devices.html
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2

"""

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

# operating modes
NON_INTERACTIVE_MODE = 0
INTERACTIVE_MODE = 1

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
KEY_A                   = 0x04
KEY_B                   = 0x05
KEY_C                   = 0x06
KEY_D                   = 0x07
KEY_E                   = 0x08
KEY_F                   = 0x09
KEY_G                   = 0x0A
KEY_H                   = 0x0B
KEY_I                   = 0x0C
KEY_J                   = 0x0D
KEY_K                   = 0x0E
KEY_L                   = 0x0F
KEY_M                   = 0x10
KEY_N                   = 0x11
KEY_O                   = 0x12
KEY_P                   = 0x13
KEY_Q                   = 0x14
KEY_R                   = 0x15
KEY_S                   = 0x16
KEY_T                   = 0x17
KEY_U                   = 0x18
KEY_V                   = 0x19
KEY_W                   = 0x1A
KEY_X                   = 0x1B
KEY_Y                   = 0x1C
KEY_Z                   = 0x1D
KEY_1                   = 0x1E
KEY_2                   = 0x1F
KEY_3                   = 0x20
KEY_4                   = 0x21
KEY_5                   = 0x22
KEY_6                   = 0x23
KEY_7                   = 0x24
KEY_8                   = 0x25
KEY_9                   = 0x26
KEY_0                   = 0x27
KEY_ENTER               = 0x28
KEY_ESC                 = 0x29
KEY_BACKSPACE           = 0x2A
KEY_TAB                 = 0x2B
KEY_SPACE               = 0x2C
KEY_MINUS               = 0x2D
KEY_EQUAL               = 0x2E
KEY_BRACKET_LEFT        = 0x2F
KEY_BRACKET_RIGHT       = 0x30
KEY_BACKSLASH           = 0x31
KEY_EUROPE_1            = 0x32
KEY_SEMICOLON           = 0x33
KEY_APOSTROPHE          = 0x34
KEY_GRAVE               = 0x35
KEY_COMMA               = 0x36
KEY_PERIOD              = 0x37
KEY_SLASH               = 0x38
KEY_CAPSLOCK            = 0x39
KEY_F1                  = 0x3A
KEY_F2                  = 0x3B
KEY_F3                  = 0x3C
KEY_F4                  = 0x3D
KEY_F5                  = 0x3E
KEY_F6                  = 0x3F
KEY_F7                  = 0x40
KEY_F8                  = 0x41
KEY_F9                  = 0x42
KEY_F10                 = 0x43
KEY_F11                 = 0x44
KEY_F12                 = 0x45
KEY_PRINT_SCREEN        = 0x46
KEY_SCROLLLOCK         = 0x47
KEY_PAUSE               = 0x48
KEY_INSERT              = 0x49
KEY_HOME                = 0x4A
KEY_PAGEUP             = 0x4B
KEY_DELETE              = 0x4C
KEY_END                 = 0x4D
KEY_PAGEDOWN           = 0x4E
KEY_RIGHT         = 0x4F
KEY_LEFT          = 0x50
KEY_DOWN          = 0x51
KEY_UP            = 0x52
KEY_NUMLOCK            = 0x53
KEY_KPSLASH       = 0x54
KEY_KPASTERISK     = 0x55
KEY_KPMINUS       = 0x56
KEY_KPPLUS          = 0x57
KEY_KPENTER        = 0x58
KEY_KP1            = 0x59
KEY_KP2            = 0x5A
KEY_KP3            = 0x5B
KEY_KP4            = 0x5C
KEY_KP5            = 0x5D
KEY_KP6            = 0x5E
KEY_KP7            = 0x5F
KEY_KP8            = 0x60
KEY_KP9            = 0x61
KEY_KP0            = 0x62
KEY_KPDOT          = 0x63
KEY_EUROPE_2            = 0x64
KEY_APPLICATION         = 0x65
KEY_POWER               = 0x66
KEY_KEYPAD_EQUAL        = 0x67
KEY_F13                 = 0x68
KEY_F14                 = 0x69
KEY_F15                 = 0x6A
KEY_CONTROL_LEFT        = 0xE0
KEY_SHIFT_LEFT          = 0xE1
KEY_ALT_LEFT            = 0xE2
KEY_GUI_LEFT            = 0xE3
KEY_CONTROL_RIGHT       = 0xE4
KEY_SHIFT_RIGHT         = 0xE5
KEY_ALT_RIGHT           = 0xE6
KEY_GUI_RIGHT           = 0xE7
KEY_SYSRQ               = 0xE7

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

        self.service = service
        self.pressed_key_count = 0              # initialize keypress counter
        self.mode = INTERACTIVE_MODE            # interactive mode is default
        self.selector = DefaultSelector()

    def device_add(self, args, device):
        try:
            dev = InputDevice(device.device_node)
            # print(dev.capabilities(verbose=True))
            print(dev.capabilities())
            # print(dev)
            self.selector.register(dev, selectors.EVENT_READ)
        except:# RuntimeException as e:
            import traceback
            traceback.print_exc()

    def device_remove(self, args, device):
        try:
            dev = InputDevice(device.device_node)
            # print(dev)
            self.selector.unregister(dev)
        except:
            import traceback
            traceback.print_exc()

    def change_state(self, keydata, keypress=True):
        """Change keyboard state"""

        print("key count {}".format(self.pressed_key_count))

        if keypress:
            if keydata[0] != MODIFIER_NONE and keydata[1] != KEY_NONE:
                if keydata[1] not in self.state[4:]:
                    # increase key count
                    self.pressed_key_count += 1

                    # find free key slot
                    i = self.state[4:].index(0)

                    # set key
                    self.state[4 + i] = keydata[1]
                    print("Key press {}".format(keydata[1]))

                self.state[2] = keydata[0]


            elif keydata[1] != KEY_NONE:
                if keydata[1] not in self.state[4:]:
                    # increase key count
                    self.pressed_key_count += 1

                    # find free key slot
                    i = self.state[4:].index(0)

                    # set key
                    self.state[4 + i] = keydata[1]
                    print("Key press {}".format(keydata[1]))

            elif keydata[0] != MODIFIER_NONE and keydata[1] == KEY_NONE:
                # process modifier keys
                print("{} pressed".format(keydata[0]))

                self.state[2] |= keydata[0]
                print("Modify modifier byte {}".format(self.state[2]))

            elif keydata[2] != 0:
                self.service.send_mouse(keydata[2], 0, 0, 0)
                return

        else:
            if keydata[1] != KEY_NONE:
                # decrease keypress count
                self.pressed_key_count -= 1
                print("Key release {}".format(keydata[1]))

                # update state
                i = self.state[4:].index(keydata[1])
                self.state[4 + i] = 0

            if keydata[0] != MODIFIER_NONE:
                print("{} released".format(keydata[0]))
                self.state[2] &= ~keydata[0]

            elif keydata[2] != 0:
                self.service.send_mouse(0, 0, 0, 0)
                return


        # print(self)
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
                            print('E', event.type, event.value, event.code, "0x%02x" % event.code)
                            ce = evdev.util.categorize(event)
                            print(ce.scancode, ce.keystate, ce.keycode)

                            key = key_from_event(ce)
                            if event.value == 0:
                                self.on_release(key)
                            elif event.value == 1:
                                self.on_press(key)
                        elif event.type == ecodes.EV_REL:
                            print('E', event.type, event.value, event.code, "0x%02x" % event.code)
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
                            print("X", event)

        except KeyboardInterrupt:
            pass

    def __str__(self):
        """Keyboard state as string"""

        return repr(self.state)

mapping = {
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
    'BTN_MIDDLE': 2,
    'BTN_RIGHT': 4,
    272: 1,
    273: 2,
    274: 4
}

def key_from_event(e):
    k = e.keycode

    if isinstance(k, list):
        k = k[0]

    if k in mapping:
        return [LOOKUP[k], KEY_NONE, 0]

    v = LOOKUP.get(k)
    if v:
        print('lookup', k, v)
        return [MODIFIER_NONE, v, 0]

    v = mouse_mapping.get(k)
    if v:
        return [MODIFIER_NONE, KEY_NONE, v]

    print("*** Missing", e)
    return [MODIFIER_NONE, KEY_NONE, 0]

# main
if __name__ == "__main__":
    print("[*] Intialize keyboard")
    kbd = Keyboard()

    print("[*] Start event loop ...")
    kbd.event_loop()
