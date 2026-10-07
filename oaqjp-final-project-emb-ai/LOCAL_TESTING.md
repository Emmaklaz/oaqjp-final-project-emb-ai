# Local testing

The Watson endpoint may be unavailable. Do not claim a live Watson request succeeded if it did not.

The unit tests mock the Watson response:

```bash
python -m unittest -v
```

Test the package import:

```bash
python -c "import EmotionDetection; from EmotionDetection.emotion_detection import emotion_detector; print('EmotionDetection package:', EmotionDetection); print('emotion_detector:', emotion_detector)"
```

Test blank input locally without Watson:

```bash
python -c "from server import app; c=app.test_client(); print(c.get('/emotionDetector').data.decode())"
```

Expected:

```text
Invalid input! Try again.
```
