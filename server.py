from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LT_API = "https://libretranslate.de/translate"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)