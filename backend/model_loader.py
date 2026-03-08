# import tensorflow as tf

# MODEL_PATH = "besttrainedmodel.h5"

# model = tf.keras.models.load_model(MODEL_PATH)

# def predict(img_tensor):
#     prob = model.predict(img_tensor)[0][0]
#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob
#     return label, float(confidence
import tensorflow as tf
import os
import gdown

MODEL_PATH = "besttrainedmodel.h5"
FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

print("Loading model...")
model = tf.keras.models.load_model(MODEL_PATH)

def predict(img_tensor):
    prob = model.predict(img_tensor)[0][0]
    label = "Fake" if prob > 0.5 else "Real"
    confidence = prob if prob > 0.5 else 1 - prob
    return label, float(confidence)

