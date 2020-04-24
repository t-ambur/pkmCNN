import ctypes
import time

# This class handles keyboard input to the emulator

# These constants are defined as follows:
# BUTTON_ON_GAMEBOY = HEX_KEYCODE that corresponds to the default keyboard map in VBA-M
# e.g. in order to press the A button we must send the key L to VBA-M, because VBA-M uses the L-key to correspond to A
# HEX codes link: http://www.flint.jp/misc/?q=dik&lang=en
A = 0x26  # 0x26 IS L
B = 0x25  # is K
UP = 0x11  # is W
DOWN = 0x1F  # is S
LEFT = 0x1E  # is A
RIGHT = 0x20  # is D
UP_LEFT = 0x17  # is I
UP_RIGHT = 0x18  # is O
SELECT = 0x0E  # is backspace
START = 0x1C  # is enter
##############
ENTER = START
ALT = 0x38  # is left alt
F_KEY = 0x21
L_KEY = A
B_KEY = 0x30
U_KEY = 0x16
E_KEY = 0x12
Z_KEY = 0x2C
I_KEY = UP_LEFT
P_KEY = 0x19
DOT_KEY = 0x34
SET_DEFAULT_SIZE = 0x05  # is 4

#####
SAFE_DELAY = 1
SHORT_DELAY = .7
DELAY = .75
TYPE_DELAY = .2
NO_DELAY = .05
FAST = .5

# This code is not originally mine, and I unfortunately do not know the original author
# This "C" code is required to emulate the low-level keystrokes required by modern emulators
# (e.g. get around DirectInput)
# Link in which I found the code:
# https://www.reddit.com/r/learnpython/comments/22tke1/use_python_to_send_keystrokes_to_games_in_windows/
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions


def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def KeyPress(keycode, delay=DELAY):
    time.sleep(delay)
    PressKey(keycode)
    time.sleep(0.05)
    ReleaseKey(keycode)
