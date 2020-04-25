import cv2
import tensorflow as tf
import constants as c


def prepare(filepath):
    IMG_SIZE = c.IMG_SIZE
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    img_array = img_array/255.0
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


def predict(filepath, model):
    prediction = model.predict_classes([prepare(filepath)])
    # print(prediction)
    index = prediction[0][0]
    return index


model = tf.keras.models.load_model(c.BTL_MODEL_PATH)
index = predict("train\\nonbattle\\atest.png", model)
print(str(c.BTL_CATEGORIES[index]))
# prediction = model.predict_classes([prepare('dog.jpg')])
