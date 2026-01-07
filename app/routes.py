from flask import render_template, request
from model import chatbot_response

def app_routes(app):

    @app.route("/", methods=["GET", "POST"])
    def home():
        bot_reply = ""
        user_msg = ""

        if request.method == "POST":
            user_msg = request.form["message"]
            bot_reply = chatbot_response(user_msg)

        return render_template("index.html",
                               user_msg=user_msg,
                               bot_reply=bot_reply)
