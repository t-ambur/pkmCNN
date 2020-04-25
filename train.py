from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
# more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time
import numpy as np
import constants as c


def load_pickles():
    pickle_in = open("X.pkl","rb")
    X = pickle.load(pickle_in)

    pickle_in = open("y.pkl","rb")
    y = pickle.load(pickle_in)
    return X, y

# after deciding which layers to choose, make these match
# dense_layers = [0]
# layer_sizes = [64]
# conv_layers = [3]


def train(dense_layers, layer_sizes, conv_layers):
    X, y = load_pickles()
    for dense_layer in dense_layers:
        for layer_size in layer_sizes:
            for conv_layer in conv_layers:
                NAME = "{}-conv-{}-nodes-{}-dense-{}".format(conv_layer, layer_size, dense_layer, int(time.time()))
                print(NAME)

                model = Sequential()

                model.add(Conv2D(layer_size, (3, 3), input_shape=X.shape[1:]))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2, 2)))

                for l in range(conv_layer-1):
                    model.add(Conv2D(layer_size, (3, 3)))
                    model.add(Activation('relu'))
                    model.add(MaxPooling2D(pool_size=(2, 2)))

                model.add(Flatten())

                for _ in range(dense_layer):
                    model.add(Dense(layer_size))
                    model.add(Activation('relu'))

                model.add(Dense(1))
                model.add(Activation('sigmoid'))

                tensorboard = TensorBoard(log_dir="logs\\{}".format(NAME))

                model.compile(loss='binary_crossentropy',
                              optimizer='adam',
                              metrics=['accuracy'],
                              )

                y = np.asarray(y)

                model.fit(X, y,
                          batch_size=c.BATCH_SIZE,
                          epochs=c.EPOCHS,
                          validation_split=c.VALIDATION_SPLIT,
                          callbacks=[tensorboard])

    model.save('CNN.model')