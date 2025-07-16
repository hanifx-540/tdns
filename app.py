from flask import Flask, request
import os

app = Flask(__name__)
SECRET_KEY = "hanifx2025"  # আপনি চাইলে strong key দিতে পারেন

@app.route("/")
def home():
    return "Welcome to Hanifx DNS Controller"

@app.route("/unlock")
def unlock():
    key = request.args.get("key")
    if key == SECRET_KEY:
        if os.path.exists("BLOCK_MODE"):
            os.remove("BLOCK_MODE")
        return "✅ Internet UNBLOCKED!"
    return "⛔ Access Denied"

@app.route("/lock")
def lock():
    key = request.args.get("key")
    if key == SECRET_KEY:
        open("BLOCK_MODE", "w").write("1")
        return "🔒 Internet BLOCKED!"
    return "⛔ Access Denied"
