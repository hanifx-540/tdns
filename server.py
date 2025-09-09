from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import secrets, os

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

# ডেমো API key storage (production: DB)
API_KEYS = {
    "test-123": "Test User"
}

# Admin secret (API key generate)
ADMIN_SECRET = "SUPERSECRETADMIN"

def real_encode(text: str) -> str:
    """Demo encode – আপনার মূল encode লজিক বসান"""
    return text[::-1]

# ===========================
# API: Encode
# ===========================
@app.route("/encode", methods=["POST"])
def encode_api():
    api_key = request.headers.get("Authorization")
    if api_key not in API_KEYS:
        return jsonify({"status":"error","message":"Invalid API Key"}), 401

    data = request.get_json()
    text = data.get("text","")
    if not text:
        return jsonify({"status":"error","message":"No text provided"}), 400

    encoded = real_encode(text)
    return jsonify({"status":"success","user":API_KEYS[api_key],"encoded":encoded})

# ===========================
# API: Generate new API key (Admin only)
# ===========================
@app.route("/generate-key", methods=["POST"])
def generate_key():
    admin_secret = request.headers.get("Admin-Secret")
    if admin_secret != ADMIN_SECRET:
        return jsonify({"error":"Unauthorized"}), 401

    data = request.get_json()
    username = data.get("username","User")
    new_key = secrets.token_hex(16)  # 32-character key
    API_KEYS[new_key] = username
    return jsonify({"message":"API Key generated","api_key":new_key,"user":username})

# ===========================
# Serve frontend
# ===========================
@app.route("/")
def home():
    return send_from_directory('frontend','index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)
