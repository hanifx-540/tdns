from flask import Flask, render_template, request, redirect, url_for, flash
import hanifx

app = Flask(__name__)
app.secret_key = "replace_with_a_random_secret"  # production এ secure করে বদলাও

@app.route("/", methods=["GET", "POST"])
def index():
    encoded = None
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("data", "").strip()
        if not user_input:
            flash("সেটাতে কিছু লিখো আগে — তারপর Encode করো।", "warning")
            return redirect(url_for("index"))
        try:
            # hanifx encode কল — তোমার মডিউলের ফাংশন নাম যদি আলাদা হয় বদলাও
            encoded = hanifx.encode(user_input)
        except Exception as e:
            flash(f"Encode করতে সমস্যা: {e}", "danger")
    return render_template("index.html", encoded=encoded, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
