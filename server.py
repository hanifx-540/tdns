from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)  # ফ্রন্টএন্ড থেকে API কল করার অনুমতি

# ডেমো API keys (চাইলে ডাটাবেজে রাখতে পারেন)
VALID_KEYS = {
    "test-123": "Test User",
    "abc-456": "Premium User"
}

def real_encode(data: str) -> str:
    """
    এখানে আপনার আসল encode লজিক বসান
    এখন ডেমো হিসেবে শুধু উল্টে দিচ্ছি
    """
    return data[::-1]

@app.route("/")
def serve_frontend():
    # ফ্রন্টএন্ডের index.html সার্ভ করবে
    return send_from_directory('frontend', 'index.html')

@app.route("/encode", methods=["POST"])
def encode():
    api_key = request.headers.get("Authorization")
    if api_key not in VALID_KEYS:
        return jsonify({"status": "error", "message": "Invalid API key"}), 401

    payload = request.get_json(silent=True)
    if not payload or "data" not in payload:
        return jsonify({"status": "error", "message": "Missing data field"}), 400

    encoded = real_encode(payload["data"])
    return jsonify({
        "status": "success",
        "user": VALID_KEYS[api_key],
        "encoded": encoded
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
