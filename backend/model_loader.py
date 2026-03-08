import tensorflow as tf
import os
import gdown

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

MODEL_PATH = "besttrainedmodel.h5"
FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"

model = None

def load_model():
global model

```
if model is not None:
    return model

# If model not present, download it
if not os.path.exists(MODEL_PATH):
    print("Model not found. Downloading from Google Drive...")
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

print("Loading deepfake detection model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully")

return model
```

def predict(img_tensor):
model = load_model()

```
prob = model.predict(img_tensor)[0][0]

label = "Fake" if prob > 0.5 else "Real"
confidence = prob if prob > 0.5 else 1 - prob

return label, float(confidence)
```

