KEY_RECORDS = [
    ['KEY_MOD_LCTRL', 0x01, ''],
    ['KEY_MOD_LSHIFT', 0x02, ''],
    ['KEY_MOD_LALT', 0x04, ''],
    ['KEY_MOD_LMETA', 0x08, ''],
    ['KEY_MOD_RCTRL', 0x10, ''],
    ['KEY_MOD_RSHIFT', 0x20, ''],
    ['KEY_MOD_RALT', 0x40, ''],
    ['KEY_MOD_RMETA', 0x80, ''],
    ['KEY_NONE', 0x00, 'No key pressed'],
    ['KEY_ERR_OVF', 0x01, 'Keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")'],
    ['KEY_A', 0x04, 'Keyboard a and A'],
    ['KEY_B', 0x05, 'Keyboard b and B'],
    ['KEY_C', 0x06, 'Keyboard c and C'],
    ['KEY_D', 0x07, 'Keyboard d and D'],
    ['KEY_E', 0x08, 'Keyboard e and E'],
    ['KEY_F', 0x09, 'Keyboard f and F'],
    ['KEY_G', 0x0A, 'Keyboard g and G'],
    ['KEY_H', 0x0B, 'Keyboard h and H'],
    ['KEY_I', 0x0C, 'Keyboard i and I'],
    ['KEY_J', 0x0D, 'Keyboard j and J'],
    ['KEY_K', 0x0E, 'Keyboard k and K'],
    ['KEY_L', 0x0F, 'Keyboard l and L'],
    ['KEY_M', 0x10, 'Keyboard m and M'],
    ['KEY_N', 0x11, 'Keyboard n and N'],
    ['KEY_O', 0x12, 'Keyboard o and O'],
    ['KEY_P', 0x13, 'Keyboard p and P'],
    ['KEY_Q', 0x14, 'Keyboard q and Q'],
    ['KEY_R', 0x15, 'Keyboard r and R'],
    ['KEY_S', 0x16, 'Keyboard s and S'],
    ['KEY_T', 0x17, 'Keyboard t and T'],
    ['KEY_U', 0x18, 'Keyboard u and U'],
    ['KEY_V', 0x19, 'Keyboard v and V'],
    ['KEY_W', 0x1A, 'Keyboard w and W'],
    ['KEY_X', 0x1B, 'Keyboard x and X'],
    ['KEY_Y', 0x1C, 'Keyboard y and Y'],
    ['KEY_Z', 0x1D, 'Keyboard z and Z'],
    ['KEY_1', 0x1E, 'Keyboard 1 and !'],
    ['KEY_2', 0x1F, 'Keyboard 2 and @'],
    ['KEY_3', 0x20, 'Keyboard 3 and #'],
    ['KEY_4', 0x21, 'Keyboard 4 and $'],
    ['KEY_5', 0x22, 'Keyboard 5 and %'],
    ['KEY_6', 0x23, 'Keyboard 6 and ^'],
    ['KEY_7', 0x24, 'Keyboard 7 and &'],
    ['KEY_8', 0x25, 'Keyboard 8 and *'],
    ['KEY_9', 0x26, 'Keyboard 9 and ('],
    ['KEY_0', 0x27, 'Keyboard 0 and )'],
    ['KEY_ENTER', 0x28, 'Keyboard Return (ENTER)'],
    ['KEY_ESC', 0x29, 'Keyboard ESCAPE'],
    ['KEY_BACKSPACE', 0x2A, 'Keyboard DELETE (Backspace)'],
    ['KEY_TAB', 0x2B, 'Keyboard Tab'],
    ['KEY_SPACE', 0x2C, 'Keyboard Spacebar'],
    ['KEY_MINUS', 0x2D, 'Keyboard - and _'],
    ['KEY_EQUAL', 0x2E, 'Keyboard = and +'],
    ['KEY_LEFTBRACE', 0x2F, 'Keyboard [ and {'],
    ['KEY_RIGHTBRACE', 0x30, 'Keyboard ] and }'],
    ['KEY_BACKSLASH', 0x31, 'Keyboard \ and |'],
    ['KEY_HASHTILDE', 0x32, 'Keyboard Non-US # and ~'],
    ['KEY_SEMICOLON', 0x33, 'Keyboard ; and :'],
    ['KEY_APOSTROPHE', 0x34, 'Keyboard \' and "'],
    ['KEY_GRAVE', 0x35, 'Keyboard ` and ~'],
    ['KEY_COMMA', 0x36, 'Keyboard , and <'],
    ['KEY_DOT', 0x37, 'Keyboard . and >'],
    ['KEY_SLASH', 0x38, 'Keyboard / and ?'],
    ['KEY_CAPSLOCK', 0x39, 'Keyboard Caps Lock'],
    ['KEY_F1', 0x3A, 'Keyboard F1'],
    ['KEY_F2', 0x3B, 'Keyboard F2'],
    ['KEY_F3', 0x3C, 'Keyboard F3'],
    ['KEY_F4', 0x3D, 'Keyboard F4'],
    ['KEY_F5', 0x3E, 'Keyboard F5'],
    ['KEY_F6', 0x3F, 'Keyboard F6'],
    ['KEY_F7', 0x40, 'Keyboard F7'],
    ['KEY_F8', 0x41, 'Keyboard F8'],
    ['KEY_F9', 0x42, 'Keyboard F9'],
    ['KEY_F10', 0x43, 'Keyboard F10'],
    ['KEY_F11', 0x44, 'Keyboard F11'],
    ['KEY_F12', 0x45, 'Keyboard F12'],
    ['KEY_SYSRQ', 0x46, 'Keyboard Print Screen'],
    ['KEY_SCROLLLOCK', 0x47, 'Keyboard Scroll Lock'],
    ['KEY_PAUSE', 0x48, 'Keyboard Pause'],
    ['KEY_INSERT', 0x49, 'Keyboard Insert'],
    ['KEY_HOME', 0x4A, 'Keyboard Home'],
    ['KEY_PAGEUP', 0x4B, 'Keyboard Page Up'],
    ['KEY_DELETE', 0x4C, 'Keyboard Delete Forward'],
    ['KEY_END', 0x4D, 'Keyboard End'],
    ['KEY_PAGEDOWN', 0x4E, 'Keyboard Page Down'],
    ['KEY_RIGHT', 0x4F, 'Keyboard Right Arrow'],
    ['KEY_LEFT', 0x50, 'Keyboard Left Arrow'],
    ['KEY_DOWN', 0x51, 'Keyboard Down Arrow'],
    ['KEY_UP', 0x52, 'Keyboard Up Arrow'],
    ['KEY_NUMLOCK', 0x53, 'Keyboard Num Lock and Clear'],
    ['KEY_KPSLASH', 0x54, 'Keypad /'],
    ['KEY_KPASTERISK', 0x55, 'Keypad *'],
    ['KEY_KPMINUS', 0x56, 'Keypad -'],
    ['KEY_KPPLUS', 0x57, 'Keypad +'],
    ['KEY_KPENTER', 0x58, 'Keypad ENTER'],
    ['KEY_KP1', 0x59, 'Keypad 1 and End'],
    ['KEY_KP2', 0x5A, 'Keypad 2 and Down Arrow'],
    ['KEY_KP3', 0x5B, 'Keypad 3 and PageDn'],
    ['KEY_KP4', 0x5C, 'Keypad 4 and Left Arrow'],
    ['KEY_KP5', 0x5D, 'Keypad 5'],
    ['KEY_KP6', 0x5E, 'Keypad 6 and Right Arrow'],
    ['KEY_KP7', 0x5F, 'Keypad 7 and Home'],
    ['KEY_KP8', 0x60, 'Keypad 8 and Up Arrow'],
    ['KEY_KP9', 0x61, 'Keypad 9 and Page Up'],
    ['KEY_KP0', 0x62, 'Keypad 0 and Insert'],
    ['KEY_KPDOT', 0x63, 'Keypad . and Delete'],
    ['KEY_102ND', 0x64, 'Keyboard Non-US \ and |'],
    ['KEY_COMPOSE', 0x65, 'Keyboard Application'],
    ['KEY_POWER', 0x66, 'Keyboard Power'],
    ['KEY_KPEQUAL', 0x67, 'Keypad ='],
    ['KEY_F13', 0x68, 'Keyboard F13'],
    ['KEY_F14', 0x69, 'Keyboard F14'],
    ['KEY_F15', 0x6A, 'Keyboard F15'],
    ['KEY_F16', 0x6B, 'Keyboard F16'],
    ['KEY_F17', 0x6C, 'Keyboard F17'],
    ['KEY_F18', 0x6D, 'Keyboard F18'],
    ['KEY_F19', 0x6E, 'Keyboard F19'],
    ['KEY_F20', 0x6F, 'Keyboard F20'],
    ['KEY_F21', 0x70, 'Keyboard F21'],
    ['KEY_F22', 0x71, 'Keyboard F22'],
    ['KEY_F23', 0x72, 'Keyboard F23'],
    ['KEY_F24', 0x73, 'Keyboard F24'],
    ['KEY_OPEN', 0x74, 'Keyboard Execute'],
    ['KEY_HELP', 0x75, 'Keyboard Help'],
    ['KEY_PROPS', 0x76, 'Keyboard Menu'],
    ['KEY_FRONT', 0x77, 'Keyboard Select'],
    ['KEY_STOP', 0x78, 'Keyboard Stop'],
    ['KEY_AGAIN', 0x79, 'Keyboard Again'],
    ['KEY_UNDO', 0x7A, 'Keyboard Undo'],
    ['KEY_CUT', 0x7B, 'Keyboard Cut'],
    ['KEY_COPY', 0x7C, 'Keyboard Copy'],
    ['KEY_PASTE', 0x7D, 'Keyboard Paste'],
    ['KEY_FIND', 0x7E, 'Keyboard Find'],
    ['KEY_MUTE', 0x7F, 'Keyboard Mute'],
    ['KEY_VOLUMEUP', 0x80, 'Keyboard Volume Up'],
    ['KEY_VOLUMEDOWN', 0x81, 'Keyboard Volume Down'],
    ['KEY_KPCOMMA', 0x85, 'Keypad Comma'],
    ['KEY_RO', 0x87, 'Keyboard International1'],
    ['KEY_KATAKANAHIRAGANA', 0x88, 'Keyboard International2'],
    ['KEY_YEN', 0x89, 'Keyboard International3'],
    ['KEY_HENKAN', 0x8A, 'Keyboard International4'],
    ['KEY_MUHENKAN', 0x8B, 'Keyboard International5'],
    ['KEY_KPJPCOMMA', 0x8C, 'Keyboard International6'],
    ['KEY_HANGEUL', 0x90, 'Keyboard LANG1'],
    ['KEY_HANJA', 0x91, 'Keyboard LANG2'],
    ['KEY_KATAKANA', 0x92, 'Keyboard LANG3'],
    ['KEY_HIRAGANA', 0x93, 'Keyboard LANG4'],
    ['KEY_ZENKAKUHANKAKU', 0x94, 'Keyboard LANG5'],
    ['KEY_KPLEFTPAREN', 0xB6, 'Keypad ('],
    ['KEY_KPRIGHTPAREN', 0xB7, 'Keypad )'],
    ['KEY_LEFTCTRL', 0xE0, 'Keyboard Left Control'],
    ['KEY_LEFTSHIFT', 0xE1, 'Keyboard Left Shift'],
    ['KEY_LEFTALT', 0xE2, 'Keyboard Left Alt'],
    ['KEY_LEFTMETA', 0xE3, 'Keyboard Left GUI'],
    ['KEY_RIGHTCTRL', 0xE4, 'Keyboard Right Control'],
    ['KEY_RIGHTSHIFT', 0xE5, 'Keyboard Right Shift'],
    ['KEY_RIGHTALT', 0xE6, 'Keyboard Right Alt'],
    ['KEY_RIGHTMETA', 0xE7, 'Keyboard Right GUI'],
    ['KEY_MEDIA_PLAYPAUSE', 0xE8, ''],
    ['KEY_MEDIA_STOPCD', 0xE9, ''],
    ['KEY_MEDIA_PREVIOUSSONG', 0xEA, ''],
    ['KEY_MEDIA_NEXTSONG', 0xEB, ''],
    ['KEY_MEDIA_EJECTCD', 0xEC, ''],
    ['KEY_MEDIA_VOLUMEUP', 0xED, ''],
    ['KEY_MEDIA_VOLUMEDOWN', 0xEE, ''],
    ['KEY_MEDIA_MUTE', 0xEF, ''],
    ['KEY_MEDIA_WWW', 0xF0, ''],
    ['KEY_MEDIA_BACK', 0xF1, ''],
    ['KEY_MEDIA_FORWARD', 0xF2, ''],
    ['KEY_MEDIA_STOP', 0xF3, ''],
    ['KEY_MEDIA_FIND', 0xF4, ''],
    ['KEY_MEDIA_SCROLLUP', 0xF5, ''],
    ['KEY_MEDIA_SCROLLDOWN', 0xF6, ''],
    ['KEY_MEDIA_EDIT', 0xF7, ''],
    ['KEY_MEDIA_SLEEP', 0xF8, ''],
    ['KEY_MEDIA_COFFEE', 0xF9, ''],
    ['KEY_MEDIA_REFRESH', 0xFA, ''],
    ['KEY_MEDIA_CALC', 0xFB, ''],
]



KEYBOARD_DESCRIPTOR = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x06,                    # Usage (Keyboard)                    2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x02,                    #  Report ID (1)                      6
    0x05, 0x08,                    #  Usage Page (LEDs)                  6
    0x19, 0x01,                    #  Usage Minimum (1)                  8
    0x29, 0x03,                    #  Usage Maximum (3)                  10
    0x15, 0x00,                    #  Logical Minimum (0)                12
    0x25, 0x01,                    #  Logical Maximum (1)                14
    0x75, 0x01,                    #  Report Size (1)                    16
    0x95, 0x03,                    #  Report Count (3)                   18
    0x91, 0x02,                    #  Output (Data,Var,Abs)              20
    0x95, 0x05,                    #  Report Count (5)                   22
    0x91, 0x01,                    #  Output (Cnst,Arr,Abs)              24
    0x05, 0x07,                    #  Usage Page (Keyboard)              26
    0x19, 0xe0,                    #  Usage Minimum (224)                28
    0x29, 0xe7,                    #  Usage Maximum (231)                30
    0x95, 0x08,                    #  Report Count (8)                   32
    0x81, 0x02,                    #  Input (Data,Var,Abs)               34
    0x75, 0x08,                    #  Report Size (8)                    36
    0x95, 0x01,                    #  Report Count (1)                   38
    0x81, 0x01,                    #  Input (Cnst,Arr,Abs)               40
    0x19, 0x00,                    #  Usage Minimum (0)                  42
    0x29, 0x91,                    #  Usage Maximum (145)                44
    0x26, 0xff, 0x00,              #  Logical Maximum (255)              46
    0x95, 0x06,                    #  Report Count (6)                   49
    0x81, 0x00,                    #  Input (Data,Arr,Abs)               51
    0xc0,                          # End Collection                      53
    ]

MOUSE_DESCRIPTOR = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x02,                    # Usage (Mouse)                       2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x02,                    #  Report ID (1)                      6
    0x09, 0x01,                    #  Usage (Pointer)                    6
    0xa1, 0x00,                    #  Collection (Physical)              8
    0x05, 0x09,                    #   Usage Page (Button)               10
    0x19, 0x01,                    #   Usage Minimum (1)                 12
    0x29, 0x03,                    #   Usage Maximum (3)                 14
    0x15, 0x00,                    #   Logical Minimum (0)               16
    0x25, 0x01,                    #   Logical Maximum (1)               18
    0x95, 0x08,                    #   Report Count (8)                  20
    0x75, 0x01,                    #   Report Size (1)                   22
    0x81, 0x02,                    #   Input (Data,Var,Abs)              24
    0x05, 0x01,                    #   Usage Page (Generic Desktop)      26
    0x09, 0x30,                    #   Usage (X)                         28
    0x09, 0x31,                    #   Usage (Y)                         30
    0x09, 0x38,                    #   Usage (Wheel)                     32
    0x15, 0x81,                    #   Logical Minimum (-127)            34
    0x25, 0x7f,                    #   Logical Maximum (127)             36
    0x75, 0x08,                    #   Report Size (8)                   38
    0x95, 0x03,                    #   Report Count (3)                  40
    0x81, 0x06,                    #   Input (Data,Var,Rel)              42
    0xc0,                          #  End Collection                     44
    0xc0,                          # End Collection                      45
    ]

DESCRIPTOR_1 = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x06,                    # Usage (Keyboard)                    2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x01,                    #  Report ID (1)                      6
    0xa1, 0x00,                    #  Collection (Physical)              8
    0x05, 0x07,                    #   Usage Page (Keyboard)             10
    0x19, 0xe0,                    #   Usage Minimum (224)               12
    0x29, 0xe7,                    #   Usage Maximum (231)               14
    0x15, 0x00,                    #   Logical Minimum (0)               16
    0x25, 0x01,                    #   Logical Maximum (1)               18
    0x75, 0x01,                    #   Report Size (1)                   20
    0x95, 0x08,                    #   Report Count (8)                  22
    0x81, 0x02,                    #   Input (Data,Var,Abs)              24
    0x95, 0x01,                    #   Report Count (1)                  26
    0x75, 0x08,                    #   Report Size (8)                   28
    0x81, 0x01,                    #   Input (Cnst,Arr,Abs)              30
    0x95, 0x08,                    #   Report Count (8)                  32
    0x75, 0x08,                    #   Report Size (8)                   34
    0x15, 0x00,                    #   Logical Minimum (0)               36
    0x25, 0x65,                    #   Logical Maximum (101)             38
    0x05, 0x07,                    #   Usage Page (Keyboard)             40
    0x19, 0x00,                    #   Usage Minimum (0)                 42
    0x29, 0x65,                    #   Usage Maximum (101)               44
    0x81, 0x00,                    #   Input (Data,Arr,Abs)              46
    0xc0,                          #  End Collection                     48
    0xc0,                          # End Collection                      49
    0x05, 0x01,                    # Usage Page (Generic Desktop)        50
    0x09, 0x02,                    # Usage (Mouse)                       52
    0xa1, 0x01,                    # Collection (Application)            54
    0x85, 0x02,                    #  Report ID (2)                      56
    0x09, 0x01,                    #  Usage (Pointer)                    58
    0xa1, 0x00,                    #  Collection (Physical)              60
    0x05, 0x09,                    #   Usage Page (Button)               62
    0x19, 0x01,                    #   Usage Minimum (1)                 64
    0x29, 0x03,                    #   Usage Maximum (3)                 66
    0x15, 0x00,                    #   Logical Minimum (0)               68
    0x25, 0x01,                    #   Logical Maximum (1)               70
    0x75, 0x01,                    #   Report Size (1)                   72
    0x95, 0x03,                    #   Report Count (3)                  74
    0x81, 0x02,                    #   Input (Data,Var,Abs)              76
    0x75, 0x05,                    #   Report Size (5)                   78
    0x95, 0x01,                    #   Report Count (1)                  80
    0x81, 0x01,                    #   Input (Cnst,Arr,Abs)              82
    0x05, 0x01,                    #   Usage Page (Generic Desktop)      84
    0x09, 0x30,                    #   Usage (X)                         86
    0x09, 0x31,                    #   Usage (Y)                         88
    0x09, 0x38,                    #   Usage (Wheel)                     90
    0x15, 0x81,                    #   Logical Minimum (-127)            92
    0x25, 0x7f,                    #   Logical Maximum (127)             94
    0x75, 0x08,                    #   Report Size (8)                   96
    0x95, 0x03,                    #   Report Count (3)                  98
    0x81, 0x06,                    #   Input (Data,Var,Rel)              100
    0xc0,                          #  End Collection                     102
    0xc0,                          # End Collection                      103
]

DESCRIPTOR_2 = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x06,                    # Usage (Keyboard)                    2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x01,                    #  Report ID (1)                      6
    0x75, 0x01,                    #  Report Size (1)                    8
    0x95, 0x08,                    #  Report Count (8)                   10
    0x05, 0x07,                    #  Usage Page (Keyboard)              12
    0x19, 0xe0,                    #  Usage Minimum (224)                14
    0x29, 0xe7,                    #  Usage Maximum (231)                16
    0x15, 0x00,                    #  Logical Minimum (0)                18
    0x25, 0x01,                    #  Logical Maximum (1)                20
    0x81, 0x02,                    #  Input (Data,Var,Abs)               22
    0x95, 0x01,                    #  Report Count (1)                   24
    0x75, 0x08,                    #  Report Size (8)                    26
    0x81, 0x03,                    #  Input (Cnst,Var,Abs)               28
    0x95, 0x05,                    #  Report Count (5)                   30
    0x75, 0x01,                    #  Report Size (1)                    32
    0x05, 0x08,                    #  Usage Page (LEDs)                  34
    0x19, 0x01,                    #  Usage Minimum (1)                  36
    0x29, 0x05,                    #  Usage Maximum (5)                  38
    0x91, 0x02,                    #  Output (Data,Var,Abs)              40
    0x95, 0x01,                    #  Report Count (1)                   42
    0x75, 0x03,                    #  Report Size (3)                    44
    0x91, 0x03,                    #  Output (Cnst,Var,Abs)              46
    0x95, 0x06,                    #  Report Count (6)                   48
    0x75, 0x08,                    #  Report Size (8)                    50
    0x15, 0x00,                    #  Logical Minimum (0)                52
    0x26, 0xff, 0x00,              #  Logical Maximum (255)              54
    0x05, 0x07,                    #  Usage Page (Keyboard)              57
    0x19, 0x00,                    #  Usage Minimum (0)                  59
    0x29, 0xff,                    #  Usage Maximum (255)                61
    0x81, 0x00,                    #  Input (Data,Arr,Abs)               63
    0xc0,                          # End Collection                      65
    0x05, 0x0c,                    # Usage Page (Consumer Devices)       66
    0x09, 0x01,                    # Usage (Consumer Control)            68
    0xa1, 0x01,                    # Collection (Application)            70
    0x85, 0x03,                    #  Report ID (3)                      72
    0x15, 0x00,                    #  Logical Minimum (0)                74
    0x25, 0x01,                    #  Logical Maximum (1)                76
    0x75, 0x01,                    #  Report Size (1)                    78
    0x95, 0x0b,                    #  Report Count (11)                  80
    0x0a, 0x23, 0x02,              #  Usage (AC Home)                    82
    0x0a, 0x21, 0x02,              #  Usage (AC Search)                  85
    0x0a, 0xb1, 0x01,              #  Usage (AL Screen Saver)            88
    0x09, 0xb8,                    #  Usage (Eject)                      91
    0x09, 0xb6,                    #  Usage (Scan Previous Track)        93
    0x09, 0xcd,                    #  Usage (Play/Pause)                 95
    0x09, 0xb5,                    #  Usage (Scan Next Track)            97
    0x09, 0xe2,                    #  Usage (Mute)                       99
    0x09, 0xea,                    #  Usage (Volume Down)                101
    0x09, 0xe9,                    #  Usage (Volume Up)                  103
    0x09, 0x30,                    #  Usage (Power)                      105
    0x81, 0x02,                    #  Input (Data,Var,Abs)               107
    0x95, 0x01,                    #  Report Count (1)                   109
    0x75, 0x0d,                    #  Report Size (13)                   111
    0x81, 0x03,                    #  Input (Cnst,Var,Abs)               11
    0xc0,                          # End Collection                      115
]

DESCRIPTOR_3 = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x06,                    # Usage (Keyboard)                    2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x01,                    #  Report ID (1)                      6
    0x75, 0x01,                    #  Report Size (1)                    8
    0x95, 0x08,                    #  Report Count (8)                   10
    0x05, 0x07,                    #  Usage Page (Keyboard)              12
    0x19, 0xe0,                    #  Usage Minimum (224)                14
    0x29, 0xe7,                    #  Usage Maximum (231)                16
    0x15, 0x00,                    #  Logical Minimum (0)                18
    0x25, 0x01,                    #  Logical Maximum (1)                20
    0x81, 0x02,                    #  Input (Data,Var,Abs)               22
    0x95, 0x01,                    #  Report Count (1)                   24
    0x75, 0x08,                    #  Report Size (8)                    26
    0x81, 0x03,                    #  Input (Cnst,Var,Abs)               28
    # XXX: Disable LEDS
    # 0x95, 0x05,                    #  Report Count (5)                   30
    # 0x75, 0x01,                    #  Report Size (1)                    32
    # 0x05, 0x08,                    #  Usage Page (LEDs)                  34
    # 0x19, 0x01,                    #  Usage Minimum (1)                  36
    # 0x29, 0x05,                    #  Usage Maximum (5)                  38
    # 0x91, 0x02,                    #  Output (Data,Var,Abs)              40
    # 0x95, 0x01,                    #  Report Count (1)                   42
    # 0x75, 0x03,                    #  Report Size (3)                    44
    # 0x91, 0x03,                    #  Output (Cnst,Var,Abs)              46
    0x95, 0x06,                    #  Report Count (6)                   48
    0x75, 0x08,                    #  Report Size (8)                    50
    0x15, 0x00,                    #  Logical Minimum (0)                52
    0x26, 0xff, 0x00,              #  Logical Maximum (255)              54
    0x05, 0x07,                    #  Usage Page (Keyboard)              57
    0x19, 0x00,                    #  Usage Minimum (0)                  59
    0x29, 0xff,                    #  Usage Maximum (255)                61
    0x81, 0x00,                    #  Input (Data,Arr,Abs)               63
    0xc0,                          # End Collection                      65
    0x05, 0x01,                    # Usage Page (Generic Desktop)        50
    0x09, 0x02,                    # Usage (Mouse)                       52
    0xa1, 0x01,                    # Collection (Application)            54
    0x85, 0x02,                    #  Report ID (2)                      56
    0x09, 0x01,                    #  Usage (Pointer)                    58
    0xa1, 0x00,                    #  Collection (Physical)              60
    0x05, 0x09,                    #   Usage Page (Button)               62
    0x19, 0x01,                    #   Usage Minimum (1)                 64
    0x29, 0x03,                    #   Usage Maximum (3)                 66
    0x15, 0x00,                    #   Logical Minimum (0)               68
    0x25, 0x01,                    #   Logical Maximum (1)               70
    0x75, 0x01,                    #   Report Size (1)                   72
    0x95, 0x03,                    #   Report Count (3)                  74
    0x81, 0x02,                    #   Input (Data,Var,Abs)              76
    0x75, 0x05,                    #   Report Size (5)                   78
    0x95, 0x01,                    #   Report Count (1)                  80
    0x81, 0x01,                    #   Input (Cnst,Arr,Abs)              82
    0x05, 0x01,                    #   Usage Page (Generic Desktop)      84
    0x09, 0x30,                    #   Usage (X)                         86
    0x09, 0x31,                    #   Usage (Y)                         88
    0x09, 0x38,                    #   Usage (Wheel)                     90
    0x15, 0x81,                    #   Logical Minimum (-127)            92
    0x25, 0x7f,                    #   Logical Maximum (127)             94
    0x75, 0x08,                    #   Report Size (8)                   96
    0x95, 0x03,                    #   Report Count (3)                  98
    0x81, 0x06,                    #   Input (Data,Var,Rel)              100
    0xc0,                          #  End Collection                     102
    0xc0,                          # End Collection                      103
]

DESCRIPTOR_4 = [
    0x05, 0x01,                    # Usage Page (Generic Desktop)        0
    0x09, 0x06,                    # Usage (Keyboard)                    2
    0xa1, 0x01,                    # Collection (Application)            4
    0x85, 0x01,                    #  Report ID (1)                      6
    0x05, 0x07,                    #  Usage Page (Keyboard)              8
    0x19, 0xe0,                    #  Usage Minimum (224)                10
    0x29, 0xe7,                    #  Usage Maximum (231)                12
    0x15, 0x00,                    #  Logical Minimum (0)                14
    0x25, 0x01,                    #  Logical Maximum (1)                16
    0x75, 0x01,                    #  Report Size (1)                    18
    0x95, 0x08,                    #  Report Count (8)                   20
    0x81, 0x02,                    #  Input (Data,Var,Abs)               22
    0x95, 0x01,                    #  Report Count (1)                   24
    0x75, 0x08,                    #  Report Size (8)                    26
    0x81, 0x03,                    #  Input (Cnst,Var,Abs)               28
    0x95, 0x05,                    #  Report Count (5)                   30
    0x75, 0x01,                    #  Report Size (1)                    32
    0x05, 0x08,                    #  Usage Page (LEDs)                  34
    0x19, 0x01,                    #  Usage Minimum (1)                  36
    0x29, 0x05,                    #  Usage Maximum (5)                  38
    0x91, 0x02,                    #  Output (Data,Var,Abs)              40
    0x95, 0x01,                    #  Report Count (1)                   42
    0x75, 0x03,                    #  Report Size (3)                    44
    0x91, 0x03,                    #  Output (Cnst,Var,Abs)              46
    0x95, 0x06,                    #  Report Count (6)                   48
    0x75, 0x08,                    #  Report Size (8)                    50
    0x15, 0x00,                    #  Logical Minimum (0)                52
    0x25, 0x6d,                    #  Logical Maximum (109)              54
    0x05, 0x07,                    #  Usage Page (Keyboard)              56
    0x19, 0x00,                    #  Usage Minimum (0)                  58
    0x29, 0x6d,                    #  Usage Maximum (109)                60
    0x81, 0x00,                    #  Input (Data,Arr,Abs)               62
    0xc0,                          # End Collection                      64
    0x05, 0x0c,                    # Usage Page (Consumer Devices)       65
    0x09, 0x01,                    # Usage (Consumer Control)            67
    0xa1, 0x01,                    # Collection (Application)            69
    0x85, 0x02,                    #  Report ID (2)                      71
    0x05, 0x0c,                    #  Usage Page (Consumer Devices)      73
    0x15, 0x00,                    #  Logical Minimum (0)                75
    0x25, 0x01,                    #  Logical Maximum (1)                77
    0x75, 0x01,                    #  Report Size (1)                    79
    0x95, 0x07,                    #  Report Count (7)                   81
    0x09, 0xb5,                    #  Usage (Scan Next Track)            83
    0x09, 0xb6,                    #  Usage (Scan Previous Track)        85
    0x09, 0xb7,                    #  Usage (Stop)                       87
    0x09, 0xcd,                    #  Usage (Play/Pause)                 89
    0x09, 0xe2,                    #  Usage (Mute)                       91
    0x09, 0xe9,                    #  Usage (Volume Up)                  93
    0x09, 0xea,                    #  Usage (Volume Down)                95
    0x81, 0x02,                    #  Input (Data,Var,Abs)               97
    0x95, 0x01,                    #  Report Count (1)                   99
    0x81, 0x01,                    #  Input (Cnst,Arr,Abs)               101
    0xc0,                          # End Collection                      103
    0x05, 0x01,                    # Usage Page (Generic Desktop)        104
    0x09, 0x02,                    # Usage (Mouse)                       106
    0xa1, 0x01,                    # Collection (Application)            108
    0x09, 0x01,                    #  Usage (Pointer)                    110
    0xa1, 0x00,                    #  Collection (Physical)              112
    0x85, 0x03,                    #   Report ID (3)                     114
    0x05, 0x09,                    #   Usage Page (Button)               116
    0x19, 0x01,                    #   Usage Minimum (1)                 118
    0x29, 0x08,                    #   Usage Maximum (8)                 120
    0x15, 0x00,                    #   Logical Minimum (0)               122
    0x25, 0x01,                    #   Logical Maximum (1)               124
    0x95, 0x08,                    #   Report Count (8)                  126
    0x75, 0x01,                    #   Report Size (1)                   128
    0x81, 0x02,                    #   Input (Data,Var,Abs)              130
    0x95, 0x00,                    #   Report Count (0)                  132
    0x81, 0x03,                    #   Input (Cnst,Var,Abs)              134
    0x06, 0x00, 0xff,              #   Usage Page (Vendor Defined Page 1) 136
    0x09, 0x40,                    #   Usage (Vendor Usage 0x40)         139
    0x95, 0x02,                    #   Report Count (2)                  141
    0x75, 0x08,                    #   Report Size (8)                   143
    0x15, 0x81,                    #   Logical Minimum (-127)            145
    0x25, 0x7f,                    #   Logical Maximum (127)             147
    0x81, 0x02,                    #   Input (Data,Var,Abs)              149
    0x05, 0x01,                    #   Usage Page (Generic Desktop)      151
    0x09, 0x38,                    #   Usage (Wheel)                     153
    0x15, 0x81,                    #   Logical Minimum (-127)            155
    0x25, 0x7f,                    #   Logical Maximum (127)             157
    0x75, 0x08,                    #   Report Size (8)                   159
    0x95, 0x01,                    #   Report Count (1)                  161
    0x81, 0x06,                    #   Input (Data,Var,Rel)              163
    0x09, 0x30,                    #   Usage (X)                         165
    0x09, 0x31,                    #   Usage (Y)                         167
    0x16, 0x01, 0xf8,              #   Logical Minimum (-2047)           169
    0x26, 0xff, 0x07,              #   Logical Maximum (2047)            172
    0x75, 0x0c,                    #   Report Size (12)                  175
    0x95, 0x02,                    #   Report Count (2)                  177
    0x81, 0x06,                    #   Input (Data,Var,Rel)              179
    0xc0,                          #  End Collection                     181
    0xc0,                          # End Collection                      182
]


