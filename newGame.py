from ahk import AHK
from subprocess import Popen
import os
import time
import keyInjector as KI
import constants as C
#  from ahk.window import Window
# wsh = comclt.Dispatch("WScript.Shell")

class NewGame:
    def __init__(self):
        self.ahk = AHK()
        self.emulator = None
        if os.path.exists(C.EMULATOR_LOCATION):
            print("Booting emulator...")
            self.emulator = Popen(C.EMULATOR_LOCATION, cwd=r"emulator")
            time.sleep(C.EMULATOR_BOOT_DELAY)
            print("Booted.")
        else:
            print("Could not find emulator. Should be at: ", C.EMULATOR_LOCATION)
            quit()
        self.window = self.ahk.win_get(C.EMULATOR_NAME)
        self.window.activate()

    def insert_card(self):
        print("inserting card...")
        # file -> open
        KI.KeyPress(KI.ALT, KI.SAFE_DELAY)
        KI.KeyPress(KI.F_KEY, KI.SHORT_DELAY)
        KI.KeyPress(KI.ENTER, KI.SHORT_DELAY)
        # type the ROM name, press enter
        KI.KeyPress(KI.B_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.L_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.U_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.E_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.DOT_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.Z_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.I_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.P_KEY, KI.TYPE_DELAY)
        KI.KeyPress(KI.ENTER, KI.SHORT_DELAY)
        # set default window size
        KI.KeyPress(KI.SET_DEFAULT_SIZE, KI.SHORT_DELAY)
        # wait for intro cinematic?
        if C.CINEMATIC_DELAY:
            print("waiting for cinematic...")
            time.sleep(20)
        else:
            print("doing my best to skip this cinematic...")
            print("waiting...")
            time.sleep(6)
            print("skipping")
            KI.KeyPress(KI.START)
            print("waiting...")
            time.sleep(4.5)
        print("Entering title menu...")
        KI.KeyPress(KI.START)
        time.sleep(3)
        KI.KeyPress(KI.START, KI.SHORT_DELAY)
        time.sleep(1.5)
        print("At title menu.")

    # setup the options to make the text faster
    # this results in shorter delays for keystrokes, enabling less waiting
    def titleOptions(self):
        print("setting up the options to favor me...")
        KI.KeyPress(KI.DOWN)
        KI.KeyPress(KI.DOWN)
        KI.KeyPress(KI.A)
        KI.KeyPress(KI.LEFT)
        KI.KeyPress(KI.LEFT)
        KI.KeyPress(KI.DOWN)
        KI.KeyPress(KI.DOWN)
        KI.KeyPress(KI.RIGHT)
        KI.KeyPress(KI.DOWN)
        KI.KeyPress(KI.A)
        print("waiting...")
        time.sleep(1)
        print("Done.")

    # speed our way through the text blocks at the beginning of the game
    def startNewGame(self):
        print("Lets get through these text blocks...")
        KI.KeyPress(KI.A)
        print("Waiting...")
        time.sleep(2.4)
        print("Spamming B Button")
        for i in range(0, 24, 1):
            KI.KeyPress(KI.B, KI.FAST)
        print("Time to enter our name...")
        KI.KeyPress(KI.A, KI.FAST)
        KI.KeyPress(KI.A, KI.SAFE_DELAY)
        KI.KeyPress(KI.LEFT, KI.FAST)
        KI.KeyPress(KI.A, KI.FAST)
        KI.KeyPress(KI.UP, KI.FAST)
        KI.KeyPress(KI.UP, KI.FAST)
        KI.KeyPress(KI.LEFT, KI.FAST)
        KI.KeyPress(KI.A, KI.FAST)
        print("What a great name!")
        time.sleep(1)
        KI.KeyPress(KI.A, KI.FAST)
        time.sleep(2)
        for i in range(0, 8, 1):
            KI.KeyPress(KI.B, KI.FAST)
        print("Red? What an atrocious color.")
        KI.KeyPress(KI.DOWN, KI.SAFE_DELAY)
        KI.KeyPress(KI.A, KI.FAST)
        print("This guy really likes to talk...")
        for i in range(0, 20, 1):
            KI.KeyPress(KI.B, KI.FAST)
        print("Is he done?")