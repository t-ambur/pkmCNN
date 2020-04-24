import time
import keyInjector as KI
import constants as C
import random

KEYPRESS_DELAY = KI.TYPE_DELAY

class RandomControls:
    def __init__(self, ahk):
        self.ahk = ahk

    # random focused on moving around
    def random_fast(self):
        rand = random.randint(1, 5)
        if rand <= 1:
            self.press_a()
        elif rand == 2:
            self.press_b()
        else:
            self.rand_direction(2)

    # random focused on battle and text boxes
    def rand_sequence(self):
        rand = random.randint(1, 2)
        if rand <= 1:
            self.press_a()
            self.rand_direction(1)
        else:
            self.press_b()
            self.rand_direction(1)

    # sends a random direction from the keyboard
    def rand_direction(self, times):
        rand = random.randint(1, 4)
        if rand <= 1:
            for i in range(0, times, 1):
                self.press_down()
        elif rand == 2:
            for i in range(0, times, 1):
                self.press_up()
        elif rand == 3:
            for i in range(0, times, 1):
                self.press_left()
        else:
            for i in range(0, times, 1):
                self.press_right()

    def press_a(self):
        KI.KeyPress(KI.A, KEYPRESS_DELAY)

    def press_b(self):
        KI.KeyPress(KI.B, KEYPRESS_DELAY)

    def press_down(self):
        KI.KeyPress(KI.DOWN, KEYPRESS_DELAY)

    def press_up(self):
        KI.KeyPress(KI.UP, KEYPRESS_DELAY)

    def press_left(self):
        KI.KeyPress(KI.LEFT, KEYPRESS_DELAY)

    def press_right(self):
        KI.KeyPress(KI.RIGHT, KEYPRESS_DELAY)
