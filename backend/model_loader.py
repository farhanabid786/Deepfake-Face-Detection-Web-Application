# import os
# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# os.environ["OMP_NUM_THREADS"] = "1"
# os.environ["TF_NUM_INTRAOP_THREADS"] = "1"
# os.environ["TF_NUM_INTEROP_THREADS"] = "1"

# import tensorflow as tf
# import gdown

# MODEL_PATH = "besttrainedmodel.h5"
# FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"

# model = None


# def load_model():
#     global model

#     if model is not None:
#         return model

#     if not os.path.exists(MODEL_PATH):
#         print("Model not found. Downloading from Google Drive...")
#         url = f"https://drive.google.com/uc?id={FILE_ID}"
#         gdown.download(url, MODEL_PATH, quiet=False)

#     print("Loading deepfake detection model...")
#     model = tf.keras.models.load_model(MODEL_PATH)
#     print("Model loaded successfully")

#     return model


# def predict(img_tensor):
#     model = load_model()

#     prob = model.predict(img_tensor)[0][0]

#     label = "Fake" if prob > 0.5 else "Real"
#     confidence = prob if prob > 0.5 else 1 - prob

#     return label, float(confidence)


import os
import numpy as np
import gdown
import tensorflow as tf

MODEL_PATH = "besttrainedmodel.tflite"
FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"

interpreter = None


def load_model():
    global interpreter

    if interpreter is not None:
        return interpreter

    if not os.path.exists(MODEL_PATH):
        print("Downloading TFLite model...")
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, MODEL_PATH, quiet=False)

    print("Loading TFLite model...")
    interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
    interpreter.allocate_tensors()

    return interpreter


def predict(img_tensor):

    interpreter = load_model()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], img_tensor.astype(np.float32))

    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])

    prob = float(output_data[0][0])

    label = "Fake" if prob > 0.5 else "Real"
    confidence = prob if prob > 0.5 else 1 - prob

    return label, confidence

