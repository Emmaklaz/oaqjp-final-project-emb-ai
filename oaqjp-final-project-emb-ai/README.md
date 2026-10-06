# Final project

IBM Watson NLP Emotion Detection application.

## Project structure

- `EmotionDetection/emotion_detection.py` - Watson NLP emotion detection function.
- `EmotionDetection/__init__.py` - EmotionDetection package initializer.
- `test_emotion_detection.py` - Unit tests.
- `server.py` - Flask web server.
- `templates/index.html` - Web interface.
- `static/mywebscript.js` - Browser-side interaction.
- `requirements.txt` - Python dependencies.

## Run

```bash
python -m pip install -r requirements.txt
python server.py
```

Then open http://127.0.0.1:5000

## Test

```bash
python -m unittest test_emotion_detection.py
pylint server.py
```

The Watson NLP service requires internet access.
