"""Unit tests for the Watson NLP emotion detector."""

import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test the dominant emotion for representative inputs."""

    def test_joy(self):
        """Test a joyful sentence."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test an angry sentence."""
        result = emotion_detector("I am furious about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Test a disgusted sentence."""
        result = emotion_detector("This is disgusting")
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_fear(self):
        """Test a fearful sentence."""
        result = emotion_detector("I am terrified")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_sadness(self):
        """Test a sad sentence."""
        result = emotion_detector("I am very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")


if __name__ == "__main__":
    unittest.main()
