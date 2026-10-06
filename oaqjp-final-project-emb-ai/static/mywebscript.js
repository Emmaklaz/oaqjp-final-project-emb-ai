const button = document.getElementById("analyzeButton");
const textInput = document.getElementById("textToAnalyze");
const responseBox = document.getElementById("response");

button.addEventListener("click", async () => {
    const text = textInput.value;

    try {
        const response = await fetch(
            `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`
        );
        const result = await response.text();
        responseBox.textContent = result;
    } catch (error) {
        responseBox.textContent =
            "Unable to contact the emotion detection server.";
    }
});
