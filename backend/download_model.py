# import gdown
# import os

# FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"
# MODEL_PATH = "besttrainedmodel.h5"

# if not os.path.exists(MODEL_PATH):
#     print("Downloading model during build...")
#     url = f"https://drive.google.com/uc?id={FILE_ID}"
#     gdown.download(url, MODEL_PATH, quiet=False)
# else:
#     print("Model already exists")


import gdown
import os

FILE_ID = "16UMV3ATLGDiNUVvbgFGLEIJ2XguHnZ39"
MODEL_PATH = "besttrainedmodel.tflite"

if not os.path.exists(MODEL_PATH):

    print("Downloading model during build...")

    url = f"https://drive.google.com/uc?id={FILE_ID}"

    gdown.download(url, MODEL_PATH, quiet=False)

else:

    print("Model already exists")
