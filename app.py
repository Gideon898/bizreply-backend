from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():

    data = request.json
    message = data.get("message")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": "You are BizReply AI. Reply professionally: " + message
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)
    result = response.json()

    try:
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        reply = "Error generating response"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run()
