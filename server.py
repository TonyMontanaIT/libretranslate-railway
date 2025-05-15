from flask import Flask, request, jsonify
import requests
import traceback

app = Flask(__name__)

LT_API = "https://libretranslate.de/translate"

@app.route("/")
def home():
    return "Translation API is working"

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

        response.raise_for_status()  # выбросит ошибку если статус не 200
        result = response.json()
        return jsonify(result)

    except Exception as e:
        traceback.print_exc()  # логируем ошибку в консоль Railway
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

  