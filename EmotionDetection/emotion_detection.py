import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)

    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    if response.status_code == 200:
        response_dict = json.loads(response.text)
        emotion_predictions = response_dict.get("emotionPredictions", [])
        if not emotion_predictions:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None
            }

        emotions = emotion_predictions[0].get("emotion", {})
        anger_score = emotions.get("anger", 0.0)
        disgust_score = emotions.get("disgust", 0.0)
        fear_score = emotions.get("fear", 0.0)
        joy_score = emotions.get("joy", 0.0)
        sadness_score = emotions.get("sadness", 0.0)

        emotion_scores = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        return {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score,
            "dominant_emotion": dominant_emotion
        }
    
    return {
        "anger": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "joy": 0.0,
        "sadness": 0.0,
        "dominant_emotion": "Error"
    }
    
    