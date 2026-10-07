import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


def mock_response(dominant):
    scores = {
        "anger": 0.01, "disgust": 0.01, "fear": 0.01,
        "joy": 0.01, "sadness": 0.01,
    }
    scores[dominant] = 0.90
    response = Mock()
    response.status_code = 200
    response.json.return_value = {"emotionPredictions": [{"emotion": scores}]}
    return response


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, post):
        post.return_value = mock_response("joy")
        self.assertEqual(
            emotion_detector("I am glad this happened")["dominant_emotion"],
            "joy",
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, post):
        post.return_value = mock_response("anger")
        self.assertEqual(
            emotion_detector("I am furious about this")["dominant_emotion"],
            "anger",
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, post):
        post.return_value = mock_response("disgust")
        self.assertEqual(
            emotion_detector("This is disgusting")["dominant_emotion"],
            "disgust",
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, post):
        post.return_value = mock_response("fear")
        self.assertEqual(
            emotion_detector("I am terrified")["dominant_emotion"],
            "fear",
        )

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, post):
        post.return_value = mock_response("sadness")
        self.assertEqual(
            emotion_detector("I am very sad")["dominant_emotion"],
            "sadness",
        )


if __name__ == "__main__":
    unittest.main()
