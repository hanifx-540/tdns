from flask import Flask, render_template, request, jsonify
import hanifx  # HanifX 24.0.0

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json.get('text', '')
    if not data:
        return jsonify({'error': 'No text provided!'}), 400
    try:
        encoded = hanifx.encode(data)  # HanifX encode
        return jsonify({'result': encoded})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decode', methods=['POST'])
def decode():
    data = request.json.get('text', '')
    if not data:
        return jsonify({'error': 'No text provided!'}), 400
    try:
        decoded = hanifx.decode(data)  # HanifX decode
        return jsonify({'result': decoded})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
