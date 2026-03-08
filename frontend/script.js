const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const resultBox = document.getElementById("result");
const loader = document.getElementById("loader");

/* change this if backend url changes */
const API_URL = "https://deepfake-detector-i5st.onrender.com/predict";

/* preview uploaded image */

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

    resultBox.classList.add("hidden");
    loader.classList.remove("hidden");

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    try {

        const response = await fetch(API_URL, {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loader.classList.add("hidden");

        resultBox.innerHTML = `
            Prediction: <b>${data.prediction}</b><br>
            Confidence: <b>${data.confidence}%</b>
        `;

        resultBox.className = "result " + (data.prediction === "Fake" ? "fake" : "real");

    } catch (error) {

        loader.classList.add("hidden");

        resultBox.innerHTML = "Server error or backend is sleeping.";
        resultBox.className = "result error";
    }

}
