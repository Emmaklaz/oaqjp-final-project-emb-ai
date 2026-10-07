"""Watson NLP emotion detection application."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"


def emotion_detector(text_to_analyse):
    """Analyze text and return five emotion scores and dominant emotion."""
    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(
        WATSON_URL, headers=headers, json=input_json, timeout=30
    )

    if response.status_code == 400:
        return {
            "anger": None, "disgust": None, "fear": None,
            "joy": None, "sadness": None, "dominant_emotion": None,
        }

    response.raise_for_status()
    emotions = response.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotion,
    }
