"""Flask server for the Watson NLP emotion detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_endpoint():
    """Analyze submitted text and return its detected emotions."""
    text_to_analyse = request.args.get("textToAnalyze")

    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyse)

    return str(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
