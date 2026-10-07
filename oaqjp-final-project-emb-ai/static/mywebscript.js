document.getElementById("analyzeButton").addEventListener("click", function () {
    const text = document.getElementById("textToAnalyze").value;
    const responseDiv = document.getElementById("response");

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(text))
        .then(response => response.text())
        .then(data => {
            responseDiv.textContent = data;
        })
        .catch(() => {
            responseDiv.textContent = "Unable to process the request.";
        });
});
