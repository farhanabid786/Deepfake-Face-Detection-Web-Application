import tensorflow as tf

# MODEL_PATH = "besttrainedmodel.h5"

# model = tf.keras.models.load_model(MODEL_PATH)

# def predict(img_tensor):
#     prob = model.predict(img_tensor)[0][0]
#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob
#     return label, float(confidenceimport tensorflow as tf
# import os
# import gdown

# MODEL_PATH = "besttrainedmodel.h5"
# FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"

# model = None

# def load_model():
#     global model

#     if model is not None:
#         return model

#     if not os.path.exists(MODEL_PATH):
#         print("Downloading model from Google Drive...")
#         url = f"https://drive.google.com/uc?id={FILE_ID}"
#         gdown.download(url, MODEL_PATH, quiet=False)

#     print("Loading model...")
#     model = tf.keras.models.load_model(MODEL_PATH)
#     return model


# def predict(img_tensor):
#     model = load_model()
#     prob = model.predict(img_tensor)[0][0]
#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob
#     return label, float(confidence)

# def predict(img_tensor):
#     model = load_model()
#     print("Image shape:", img_tensor.shape)

#     prob = model.predict(img_tensor)[0][0]

#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob
#     return label, float(confidence)

import tensorflow as tf

MODEL_PATH = "backend/besttrainedmodel.h5"

print("Loading deepfake detection model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully")

def predict(img_tensor):
prob = model.predict(img_tensor)[0][0]

```
label = "Fake" if prob > 0.5 else "Real"
confidence = prob if prob > 0.5 else 1 - prob

return label, float(confidence)
```




