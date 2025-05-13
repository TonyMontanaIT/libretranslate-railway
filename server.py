from flask import Flask, request, jsonify
from libretranslatepy import LibreTranslateAPI

app = Flask(__name__)
lt = LibreTranslateAPI("https://libretranslate.de")  # публичный сервер для прокси

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    q = data.get("q")
    source = data.get("source", "auto")
    target = data.get("target", "en")
    format_ = data.get("format", "text")
    try:
        translated = lt.translate(q, source, target)
        return jsonify({"translatedText": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)