const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const resultBox = document.getElementById("result");

imageInput.addEventListener("change", () => {
    const file = imageInput.files[0];
    preview.src = URL.createObjectURL(file);
    preview.hidden = false;
});

async function detect() {
    if (!imageInput.files.length) {
        alert("Please upload an image first!");
        return;
    }

    resultBox.classList.add("hidden");

    const formData = new FormData();
    formData.append("file", imageInput.files[0]);

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    resultBox.innerHTML = `
        Prediction: <b>${data.prediction}</b><br>
        Confidence: <b>${data.confidence}%</b>
    `;

    resultBox.className = "result " + (data.prediction === "Fake" ? "fake" : "real");
}
