# Deepfake Face Detection Web Application

A deep learning–based web application that detects whether a given face image is **Real or Fake (Deepfake)** using a fine-tuned **ResNet50** model.  
The system provides high accuracy and a clean web interface built with **FastAPI** and **HTML/CSS/JavaScript**.

---

## 🚀 Features
- Detects deepfake face images with high accuracy (~97%)
- Deep Learning model using Transfer Learning (ResNet50)
- FastAPI backend for inference
- Simple and responsive frontend
- Confidence score for each prediction
- Easy to run on localhost

---

## 🧠 Model Details
- Architecture: ResNet50 (pretrained on ImageNet)
- Framework: TensorFlow & Keras
- Input Size: 224 × 224
- Output: Binary classification  
  - `Real`
  - `Fake`
- Loss Function: Binary Cross Entropy
- Optimizer: Adam

---

## 🛠️ Technology Stack

| Layer      | Technology |
|------------|-----------|
| Model      | TensorFlow, Keras |
| Backend    | FastAPI |
| Frontend   | HTML, CSS, JavaScript |
| Server     | Uvicorn |
| Platform   | Localhost |

---
## 🗃️ Dataset Used

This project uses a combined dataset of multiple real and fake face image sources to create a large, diverse, and balanced dataset for training and testing the deep learning model. The following publicly available datasets from Kaggle were used:
| Dataset                                | Source                                                                                                                                                                   | Description                                                                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **140K Real and Fake Faces**           | [https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces](https://www.kaggle.com/datasets/xhlulu/140k-real-and-fake-faces)                                       | A large dataset containing 140,000 face images, split between real and fake. Used to provide a high-volume training base for both classes. |
| **Deepfake and Real Images**           | [https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images](https://www.kaggle.com/datasets/manjilkarki/deepfake-and-real-images)                             | Contains labeled deepfake images and real face images. Adds diversity in deepfake generation techniques.                                   |
| **HardFake vs Real Faces**             | [https://www.kaggle.com/datasets/hamzaboulahia/hardfakevsrealfaces](https://www.kaggle.com/datasets/hamzaboulahia/hardfakevsrealfaces)                                   | A challenging dataset with hard-to-detect fake images. Used to improve model robustness.                                                   |
| **Real and Fake Face Detection**       | [https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection](https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection)                               | Balanced dataset of real and fake faces tailored for binary classification tasks like this project.                                        |
| **Real vs AI-Generated Faces Dataset** | [https://www.kaggle.com/datasets/philosopher0808/real-vs-ai-generated-faces-dataset](https://www.kaggle.com/datasets/philosopher0808/real-vs-ai-generated-faces-dataset) | Contains real human faces and AI-generated faces from multiple GAN models. Improves AI vs real distinction ability.                        |

---


## 📂 Project Structure


Deepfake-Face-Detection-WebApp/
│
├── backend/
│ ├── main.py
│ ├── model_loader.py
│ ├── utils.py
│ ├── Bestmodel.h5
│ └── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── README.md
└── .gitignore
---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/Deepfake-Face-Detection-WebApp.git
cd Deepfake-Face-Detection-WebApp

2️⃣ Backend Setup
cd backend
python -m venv venv
Activate virtual environment:

for windows - venv\Scripts\activate
for linux/macOS - source venv/bin/activate

Install dependencies - pip install -r requirements.txt

3️⃣ Run FastAPI Server
uvicorn main:app --reload

4️⃣ Frontend Setup

Open the frontend:
cd ../frontend

Open index.html directly in browser
OR
Use VS Code Live Server


🧪 How It Works

1. User uploads a face image
2. Image is sent to FastAPI backend
3. Image preprocessing is applied
4. Trained model predicts Real or Fake
5. Result with confidence score is shown on UI

🎯 Use Cases

Detecting AI-generated fake faces
Cybercrime & digital forensics
Academic research & learning
Deepfake awareness tools

🚀 Future Enhancements

Face detection before classification
Video deepfake detection
Real-time webcam detection
Cloud deployment (AWS / Render)
Mobile app integration
