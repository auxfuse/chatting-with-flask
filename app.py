import os
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the `messages` list on line 5"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append(f"({now}) {username}: {message}")

def get_all_messages():
    """Get all messages and seperate using a `<br>`"""
    return "<br>".join(messages)

@app.route('/')
def index():
    """Main page with instructions!"""
    return render_template("index.html")

@app.route('/<username>')
def user(username):
    """Display Chat message"""
    return f"<h1>Welcome, {username}</h1>{get_all_messages()}"

@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect to the chat page"""
    add_messages(username, message)
    return redirect("/" + username)

app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)