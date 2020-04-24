from ahk import AHK
import sys
import pyscreenshot as ImageGrab
import threading
import time
####
import newGame
import randomControls as rc
import constants as c
####

# TODO
# Investigate recursive call limit in python --> taking screen shots
# Force threads to be daemons that quit (gracefully) when main app closes
# Make images alternate (1...10) then preprocess each image to save space
######## write image preprocessing
######## write first CNN

# AutoHotkey wrapper init
ahk = AHK()
# New game or continue?
starting_new = True
if len(sys.argv) > 1:
    print("AI will continue from saved game...", flush=True)
    starting_new = False
else:
    print("AI will start a new game...", flush=True)

new = newGame.StartGame(ahk)
new.insert_card()
if starting_new:
    new.titleOptions()
    new.startNewGame()
else:
    new.continue_game()

chaos = rc.RandomControls(ahk)
print("The control at this point are determined by RNG", flush=True)


def screenshot():
    threading.Timer(c.SCREEN_SHOT_INTERVAL, screenshot).start()
    window = ahk.active_window
    x = window.position[0]
    y = window.position[1]
    h = window.height
    w = window.width
    im = ImageGrab.grab(bbox=(x, y+c.SCREEN_SHOT_Y_REMOVAL, x + w, y + h))
    t = time.time()
    location = "output\\screenshot" + str(t) + ".png"
    im.save(location)
    print("Window Captured:", str(location), flush=True)


looping = True
screenshot()
while looping:
    chaos.random_fast()
