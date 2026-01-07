from flask import Flask, render_template, request
from model import chatbot_response  # your AI function

app = Flask(__name__)

# In-memory chat history
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global chat_history
    if request.method == "POST":
        user_msg = request.form["message"]
        bot_reply = chatbot_response(user_msg)

        # save chat in memory
        chat_history.append({"user": user_msg, "bot": bot_reply})

    return render_template("index.html", chat_history=chat_history)
