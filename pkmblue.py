from ahk import AHK
import sys
import pyscreenshot as ImageGrab
import threading
import tensorflow as tf
import time
####
import newGame
import controls as controls
import constants as c
import predict
####

# TODO
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

control = controls.Control(ahk)
counter = 0
current_index = 0
model = tf.keras.models.load_model(c.BTL_MODEL_PATH)


def create_daemon():
    thread = threading.Thread(name='daemon_screenshot', target=screenshot)
    thread.setDaemon(True)
    return thread


def screenshot():
    # thread = threading.Timer(c.SCREEN_SHOT_INTERVAL, screenshot)
    # thread.daemon = True
    # thread.start()
    global counter
    global current_index
    if counter > 19:
        counter = 0
    window = ahk.active_window
    x = window.position[0]
    y = window.position[1]
    h = window.height
    w = window.width
    im = ImageGrab.grab(bbox=(x, y+c.SCREEN_SHOT_Y_REMOVAL, x + w, y + h))
    location = "output\\screenshot" + str(counter) + ".png"
    im.save(location)
    t = time.time()
    #  print("Window Captured:", str(location), flush=True)
    current_index = read(location)
    t = time.time() - t
    print(str(c.BTL_CATEGORIES[current_index] + " " + str(t)), flush=True)
    counter += 1
    return


def read(image):
    global model
    return predict.predict(image, model)


looping = True
daemon = create_daemon()
daemon.start()
try:
    start = time.time()
    while looping:
        current = time.time()
        if (current - start) >= c.SCREEN_SHOT_INTERVAL:
            start = current
            if daemon.is_alive():
                daemon.join()
            daemon = create_daemon()
            daemon.start()
        #  if we are getting non-battle from CNN
        if current_index == 0:
            control.random_fast()
        else:
            control.battle_sequence()
except KeyboardInterrupt as e:
    print("Waiting for screenshot thread to close...")
    daemon.join()
    print("exiting..")
    sys.exit()
