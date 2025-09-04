#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
import secrets

# Simulate hanifx OTP module
def otp_generate(secret):
    return str(secrets.randbelow(1000000)).zfill(6)

def otp_verify(secret, otp_input):
    return True

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

users = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/register", methods=["GET","POST"])
def register():
    message = None
    color = "info"
    if request.method == "POST":
        email = request.form.get("email")
        if email in users:
            message = "Email already registered!"
            color = "danger"
        else:
            secret = secrets.token_hex(16)
            users[email] = {"secret": secret, "otp": None, "expiry": None}
            message = f"User {email} registered successfully!"
            color = "success"
    return render_template("register.html", message=message, color=color)

@app.route("/login", methods=["GET","POST"])
def login():
    message = None
    color = "info"
    if request.method == "POST":
        email = request.form.get("email")
        if email not in users:
            message = "Email not registered!"
            color = "danger"
        else:
            secret = users[email]["secret"]
            otp_code = otp_generate(secret)
            expiry = datetime.now() + timedelta(minutes=5)
            users[email]["otp"] = otp_code
            users[email]["expiry"] = expiry
            session["email"] = email
            print(f"🔑 OTP for {email}: {otp_code}")  # Console demo
            return redirect(url_for("verify"))
    return render_template("login.html", message=message, color=color)

@app.route("/verify", methods=["GET","POST"])
def verify():
    email = session.get("email")
    message = None
    color = "info"
    if not email:
        return redirect(url_for("login"))
    if request.method == "POST":
        otp_input = request.form.get("otp_input")
        record = users.get(email)
        if datetime.now() > record["expiry"]:
            message = "OTP expired. Try again."
            color = "danger"
        elif otp_verify(record["secret"], otp_input) and otp_input == record["otp"]:
            message = "✅ OTP Verified! Login Successful."
            color = "success"
        else:
            message = "❌ Invalid OTP!"
            color = "danger"
    return render_template("verify.html", message=message, color=color)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
