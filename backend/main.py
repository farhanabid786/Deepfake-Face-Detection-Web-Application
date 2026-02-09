from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import io

from model_loader import predict
from utils import preprocess_image

app = FastAPI(title="Deepfake Face Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_tensor = preprocess_image(io.BytesIO(image_bytes))
    label, confidence = predict(img_tensor)

    return {
        "prediction": label,
        "confidence": round(confidence * 100, 2)
    }
