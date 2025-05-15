from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

import logging
logging.basicConfig(level=logging.DEBUG)

LT_API = "https://libretranslate.de/translate"

# Проверка, что сервер запущен
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Server is running."})

# Перевод текста
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    try:
        response = requests.post(LT_API, json={
            "q": data.get("q", ""),
            "source": data.get("source", "auto"),
            "target": data.get("target", "en"),
            "format": data.get("format", "text")
        }, timeout=10)
        result = response.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500



