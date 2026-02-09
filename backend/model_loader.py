import tensorflow as tf

MODEL_PATH = "besttrainedmodel.h5"

model = tf.keras.models.load_model(MODEL_PATH)

def predict(img_tensor):
    prob = model.predict(img_tensor)[0][0]
    label = "Fake" if prob > 0.5 else "Real"
    confidence = prob if prob > 0.5 else 1 - prob
    return label, float(confidence)
