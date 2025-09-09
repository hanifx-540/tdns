from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import secrets, os
import hanifx  # HanifX 24.0.0 module

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

USER_API_KEYS = {}    # username: api_key
VALID_API_KEYS = {}   # all valid keys
ADMIN_SECRET = "SUPERSECRETADMIN"

# ===========================
# Encode API
# ===========================
@app.route("/encode", methods=["POST"])
def encode_api():
    api_key = request.headers.get("Authorization")
    if api_key not in VALID_API_KEYS:
        return jsonify({"status":"error","message":"Invalid API Key"}), 401

    data = request.get_json()
    text = data.get("text","")
    if not text:
        return jsonify({"status":"error","message":"No text provided"}), 400

    try:
        encoded = hanifx.encode(text)  # HanifX encode function
    except Exception as e:
        return jsonify({"status":"error","message":str(e)}), 500

    return jsonify({"status":"success","user":VALID_API_KEYS[api_key],"encoded":encoded})

# ===========================
# User API Key generate
# ===========================
@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data.get("username")
    if not username:
        return jsonify({"error":"Username required"}), 400

    if username in USER_API_KEYS:
        key = USER_API_KEYS[username]
        return jsonify({"message":"Existing API key","api_key":key})

    new_key = secrets.token_hex(16)
    USER_API_KEYS[username] = new_key
    VALID_API_KEYS[new_key] = username
    return jsonify({"message":"API key generated successfully","api_key":new_key})

# ===========================
# Admin API Key generate
# ===========================
@app.route("/generate-key", methods=["POST"])
def generate_key():
    admin_secret = request.headers.get("Admin-Secret")
    if admin_secret != ADMIN_SECRET:
        return jsonify({"error":"Unauthorized"}), 401

    data = request.get_json()
    username = data.get("username","AdminUser")
    new_key = secrets.token_hex(16)
    USER_API_KEYS[username] = new_key
    VALID_API_KEYS[new_key] = username
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
