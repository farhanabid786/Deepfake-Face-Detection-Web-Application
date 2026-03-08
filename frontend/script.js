const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const resultBox = document.getElementById("result");

const API_URL = "https://deepfake-detector-i5st.onrender.com/predict";

// Preview uploaded image
imageInput.addEventListener("change", () => {

    const file = imageInput.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);
    preview.hidden = false;
});

async function detect() {

    if (!imageInput.files.length) {
        alert("Please upload an image first!");
        return;
    }

    resultBox.className = "result";
    resultBox.innerHTML = "Analyzing image...";
    resultBox.classList.remove("hidden");

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Server error");
        }

        const data = await response.json();

        resultBox.innerHTML = `
            Prediction: <b>${data.prediction}</b><br>
            Confidence: <b>${data.confidence}%</b>
        `;

        resultBox.className = "result " + (data.prediction === "Fake" ? "fake" : "real");

    } catch (error) {

        resultBox.innerHTML = "Error connecting to server.";
        resultBox.className = "result error";

        console.error(error);
    }
}
