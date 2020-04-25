import numpy as np
import os
import random
import cv2  # for image manipulation
import pickle
import constants as c

# train holds all folders containing labels
DATADIR = "train"
# resize to a square IMG_SIZE x IMG_SIZE
IMG_SIZE = c.IMG_SIZE
training_data = []


def create_training_data(CATEGORIES):
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        index = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img),
                                       cv2.IMREAD_GRAYSCALE)  # convert to array, convert to greyscale
                img_array = img_array/255  # normalize
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize
                training_data.append([new_array, index])
            except Exception as e:
                print(str(img), "could not preprocess", flush=True)
                pass


def prep(categories):
    print("preparing images...", flush=True)
    create_training_data(categories)
    print("shuffling data", flush=True)
    random.shuffle(training_data)
    X = []  # capital X is your feature set
    y = []  # lowercase y is your labels
    print("generating pickle files...", flush=True)
    for features, label in training_data:
        X.append(features)
        y.append(label)

    X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # -1 for any number, 1 for grayscale (3 for RGB)
    return X, y


def save(X, y, location):
    outputlocation = os.path.join(location, c.X_NAME)
    pickle_out = open(outputlocation, 'wb')
    pickle.dump(X, pickle_out)
    pickle_out.close()
    print("X done.", flush=True)
    outputlocation = os.path.join(location, c.Y_NAME)
    pickle_out = open(outputlocation, 'wb')
    pickle.dump(y, pickle_out)
    pickle_out.close()
    print("Y done.\nPrepare complete.", flush=True)
    training_data.clear()


#  Battle or non-battle
print("Preparing Battle vs nonBattle", flush=True)
X, y = prep(c.BTL_CATEGORIES)
save(X, y, c.BTL_PATH)
print("Preparing World Text vs nonText", flush=True)
X, y = prep(c.TEXT_CATEGORIES)
save(X, y, c.TEXT_PATH)
