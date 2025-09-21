import sys
# Render বা অন্য hosting server-এর জন্য path ঠিক করা
sys.path.append("/opt/render/.local/lib/python3.10/site-packages")  # Python version অনুযায়ী

from flask import Flask, request, jsonify
import hanifx  # PyPI hanifx 24.0.0

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """Root endpoint"""
    return jsonify({
        "message": "Welcome to Hanifx API v24",
        "endpoints": ["/encode-text (POST)", "/encode-file (POST)"]
    })

@app.route("/encode-text", methods=["POST"])
def encode_text():
    """
    Encode text using hanifx
    """
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400
        encoded = hanifx.encode_text(text)  # tori hanifx ফাংশন অনুযায়ী নাম
        return jsonify({"encoded": encoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/encode-file", methods=["POST"])
def encode_file():
    """
    Encode file using hanifx
    """
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        content = file.read()
        encoded_file = hanifx.encode_file_content(content)  # tori hanifx ফাংশন অনুযায়ী নাম
        return jsonify({
            "filename": file.filename,
            "encoded_content": encoded_file
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
