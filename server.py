"""
Server module to deploy the Emotion Detection application.
"""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    """
    Endpoint to process emotion detection requests.
    """
    data = request.get_json()
    statement = data.get("statement", "")

    emotion_result = emotion_detector(statement)

    if emotion_result["dominant_emotion"] is None:
        return jsonify({"response": "Invalid text! Please try again."}), 400

    response_message = (
        "For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. The dominant emotion is "
        f"{emotion_result['dominant_emotion']}."
    )

    return jsonify({"response": response_message})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
