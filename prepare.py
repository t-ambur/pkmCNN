import numpy as np
import os
import random
import cv2  # for image manipulation
import pickle
import constants as c

# train holds all folders containing labels
DATADIR = "train"
# battle = label 1, nonbattle = 0
CATEGORIES = ["nonbattle", "battle"]
# path to save pkl to


# resize to a square IMG_SIZE x IMG_SIZE
IMG_SIZE = c.IMG_SIZE

training_data = []


def create_training_data():
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


print("preparing images...", flush=True)
create_training_data()
# shuffle
print("shuffling data", flush=True)
random.shuffle(training_data)

# print(len(training_data))

X = []  # capital X is your feature set
y = []  # lowercase y is your labels
print("generating pickle files...", flush=True)
for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1 for any number, 1 for grayscale (3 for RGB)

outputlocation = os.path.join(c.BTL_PATH, c.X_NAME)
pickle_out = open(outputlocation, 'wb')
pickle.dump(X, pickle_out)
pickle_out.close()
print("X done.", flush=True)

outputlocation = os.path.join(c.BTL_PATH, c.Y_NAME)
pickle_out = open(outputlocation, 'wb')
pickle.dump(y, pickle_out)
pickle_out.close()
print("Y done.\nPrepare complete.", flush=True)
