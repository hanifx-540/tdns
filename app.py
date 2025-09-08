from flask import Flask, render_template, request
import hanifx

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encoded_text = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            encoded_text = hanifx.encode(text)
    return render_template("index.html", encoded=encoded_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
