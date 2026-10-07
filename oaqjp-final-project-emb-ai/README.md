# Final project

## Emotion Detection Application

A Flask web application that uses the Watson NLP emotion detection service to analyze text for anger, disgust, fear, joy, and sadness, and identify the dominant emotion.

## Project Structure

```text
oaqjp-final-project-emb-ai/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
│   └── mywebscript.js
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing

```bash
python -m unittest -v
```

The unit tests mock Watson responses, so they can verify the application logic without requiring access to the remote Watson service.

## Static analysis

```bash
pylint server.py
```

## Run the application

```bash
python server.py
```

Open `http://localhost:5000`.

Blank input returns:

```text
Invalid input! Try again.
```
