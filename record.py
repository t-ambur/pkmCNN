from ahk import AHK
import time
import sys
import pyscreenshot as ImageGrab
import constants as c

ahk = AHK()

SCREENSHOT_INTERVAL = 2


def screenshot():
    window = ahk.active_window
    x = window.position[0]
    y = window.position[1]
    h = window.height
    w = window.width
    im = ImageGrab.grab(bbox=(x, y+c.SCREEN_SHOT_Y_REMOVAL, x + w, y + h))
    t = time.time()
    location = "record\\screenshot" + str(t) + ".png"
    im.save(location)
    print("Window Captured:", str(location), flush=True)


looping = True
try:
    while looping:
        screenshot()
        time.sleep(SCREENSHOT_INTERVAL)
except KeyboardInterrupt as e:
    print("Waiting for screenshot thread to close...")
    print("exiting..")
    sys.exit()
