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

# resize to a square IMG_SIZE x IMG_SIZE
IMG_SIZE = c.IMG_SIZE

training_data = []


def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        label = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img),
                                       cv2.IMREAD_GRAYSCALE)  # convert to array, convert to greyscale
                img_array = img_array/255  # normalize
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize
                training_data.append([new_array, label])
            except Exception as e:
                pass


create_training_data()
# shuffle
random.shuffle(training_data)

# print(len(training_data))

X = []  # capital X is your feature set
y = []  # lowercase y is your labels

for features, label in training_data:
    X.append(features)
    y.append(label)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1) # -1 for any number, 1 for grayscale (3 for RGB)

pickle_out = open('X.pkl', 'wb')
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open('y.pkl', 'wb')
pickle.dump(y, pickle_out)
pickle_out.close()
