# import tensorflow as tf

# MODEL_PATH = "besttrainedmodel.h5"

# model = tf.keras.models.load_model(MODEL_PATH)

# def predict(img_tensor):
#     prob = model.predict(img_tensor)[0][0]
#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob
#     return label, float(confidence

import os
import tensorflow as tf
import urllib.request

MODEL_URL = "https://drive.google.com/uc?export=download&id=16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"
MODEL_PATH = "besttrainedmodel.h5"

# download model if not present
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    print("Model downloaded.")

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)

def predict(img_tensor):
    prob = model.predict(img_tensor)[0][0]
    label = "Fake" if prob > 0.5 else "Real"
    confidence = prob if prob > 0.5 else 1 - prob
    return label, float(confidence)

