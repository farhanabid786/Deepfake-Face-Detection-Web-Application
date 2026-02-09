import numpy as np
from PIL import Image

IMG_SIZE = (224, 224)

def preprocess_image(image):
    img = Image.open(image).convert("RGB")
    img = img.resize(IMG_SIZE)
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img
