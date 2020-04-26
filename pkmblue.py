from ahk import AHK
import sys
import os
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
print("Loading CNNs...", flush=True)
model1 = tf.keras.models.load_model(c.BTL_MODEL_PATH)
model2 = tf.keras.models.load_model(c.TEXT_MODEL_PATH)


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
    #  t = time.time()
    #  print("Window Captured:", str(location), flush=True)
    current_index = read(location)
    #  t = time.time() - t
    print(str(c.BTL_CATEGORIES[current_index]) + " " + str(counter), flush=True)
    counter += 1
    return


def read(image):
    global model1
    return predict.predict(image, model1)


looping = True
# run one thread to make sure an image exists
daemon = create_daemon()
daemon.start()
daemon.join()
report = ""
#  loop until keyboard interrupt
try:
    start = time.time()
    while looping:
        current = time.time()
        if (current - start) >= c.SCREEN_SHOT_INTERVAL:
            report = ""
            start = current
            if daemon.is_alive():
                daemon.join()
            daemon = create_daemon()
            daemon.start()
            #  if we are getting non-battle from CNN
            if current_index == 0:
                scsht = counter - 1
                if scsht < 0:
                    scsht = 19
                loc = "output\\screenshot" + str(scsht) + ".png"
                if not os.path.exists(loc):
                    print("Cant find path", flush=True)
                    index = 0
                index = predict.predict(loc, model2)
                report = str(c.TEXT_CATEGORIES[index]) + " " + str(scsht)
                # not text
                if index == 0:
                    control.random_world()
                # text
                else:
                    control.text_sequence()
            #  we are getting battle from CNN
            else:
                control.battle_sequence()
            print(report, flush=True)
except KeyboardInterrupt as e:
    print("Waiting for screenshot thread to close...")
    daemon.join()
    print("exiting..")
    sys.exit()
