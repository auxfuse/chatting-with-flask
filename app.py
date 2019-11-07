import os
from datetime import datetime
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "randomthingystring123"
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list on line 5"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timestamp": now, "from": username, "message": message}
    messages.append(messages_dict)

@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions!"""

    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display Chat message"""
    return f"<h1>Welcome, {username}</h1>{messages}"

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)