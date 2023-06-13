import cv2
import numpy as np

from keras.models import load_model

model = load_model('batik_co_rgb_model.h5')

def prediksi(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = image.astype(np.float32) / 255.0
    image = np.expand_dims(image, axis=0)

    predictions = model.predict(image)
    r = (predictions[0][0])
    g = (predictions[0][1])
    b = (predictions[0][2])

    rgb_data = {
        'Red': round(r + np.mean(image[:, :, :, 0]) * 255),
        'Green': round(r + np.mean(image[:, :, :, 1]) * 255),
        'Blue': round(r + np.mean(image[:, :, :, 2]) * 255)
    }
    return rgb_data