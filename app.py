#!/usr/bin/env python3
from flask import Flask, render_template_string, request, session, redirect, url_for
from hanifx import otp_generate, otp_verify
import secrets
from datetime import datetime, timedelta

# -----------------------
# Terminal coloring
# -----------------------
from rich.console import Console
console = Console()

# -----------------------
# Flask app
# -----------------------
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# -----------------------
# Users storage
# -----------------------
users = {}

# -----------------------
# Redirect / to /login
# -----------------------
@app.route("/")
def home():
    return redirect(url_for("login"))

# -----------------------
# Register
# -----------------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        if email in users:
            return "<h3 style='color:red;'>Email already registered!</h3>"
        secret = secrets.token_hex(16)
        users[email] = {"secret": secret, "otp": None, "expiry": None}
        console.print(f"[bold green]Registered:[/bold green] {email}")
        return f"<h3 style='color:green;'>User {email} registered successfully!</h3>"
    return render_template_string("""
        <h2 style="color:blue;">Register</h2>
        <form method="post">
            Email: <input name="email" type="email" required>
            <button type="submit" style="background-color:green;color:white;">Register</button>
        </form>
    """)

# -----------------------
# Login / Generate OTP
# -----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        if email not in users:
            return "<h3 style='color:red;'>Email not registered!</h3>"
        secret = users[email]["secret"]
        otp_code = otp_generate(secret)
        expiry = datetime.now() + timedelta(minutes=5)
        users[email]["otp"] = otp_code
        users[email]["expiry"] = expiry
        session["email"] = email
        console.print(f"[bold yellow]OTP for {email}:[/bold yellow] {otp_code}")
        return redirect(url_for("verify"))
    return render_template_string("""
        <h2 style="color:purple;">Login</h2>
        <form method="post">
            Email: <input name="email" type="email" required>
            <button type="submit" style="background-color:orange;color:white;">Generate OTP</button>
        </form>
    """)

# -----------------------
# Verify OTP
# -----------------------
@app.route("/verify", methods=["GET", "POST"])
def verify():
    email = session.get("email")
    if not email:
        return redirect(url_for("login"))

    if request.method == "POST":
        user_input = request.form.get("otp_input")
        record = users.get(email)
        if datetime.now() > record["expiry"]:
            return "<h3 style='color:red;'>❌ OTP expired. Try again.</h3>"
        if otp_verify(record["secret"], user_input) and user_input == record["otp"]:
            console.print(f"[bold green]OTP verified for {email}[/bold green]")
            return "<h3 style='color:green;'>✅ OTP Verified. Login Successful!</h3>"
        else:
            console.print(f"[bold red]Invalid OTP for {email}[/bold red]")
            return "<h3 style='color:red;'>❌ Invalid OTP!</h3>"

    return render_template_string("""
        <h2 style="color:teal;">Enter OTP</h2>
        <form method="post">
            OTP: <input name="otp_input" type="text" required>
            <button type="submit" style="background-color:blue;color:white;">Verify</button>
        </form>
    """)

# -----------------------
# Run Flask
# -----------------------
if __name__ == "__main__":
    # For Render.com use 0.0.0.0 and port from environment variable
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
