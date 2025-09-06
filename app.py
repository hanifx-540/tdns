from flask import Flask, render_template, request
import hanifx  # secure encoder

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    encoded = None
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("data")
        if user_input:
            # hanifx encode only (no decode)
            encoded = hanifx.encode(user_input)
    return render_template("index.html", encoded=encoded, user_input=user_input)

if __name__ == "__main__":
    # Render এ চালানোর জন্য 0.0.0.0 host
    app.run(host="0.0.0.0", port=5000)
