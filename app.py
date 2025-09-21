from flask import Flask, request, jsonify
import hanifx

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to Hanifx API v24",
        "endpoints": ["/encode-text (POST)", "/encode-file (POST)"]
    })

@app.route("/encode-text", methods=["POST"])
def encode_text():
    try:
        data = request.get_json(force=True)
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "No text provided"}), 400
        encoded = hanifx.encode_text(text)
        return jsonify({"encoded": encoded})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/encode-file", methods=["POST"])
def encode_file():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        content = file.read()
        encoded_file = hanifx.encode_file_content(content)
        return jsonify({
            "filename": file.filename,
            "encoded_content": encoded_file
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
