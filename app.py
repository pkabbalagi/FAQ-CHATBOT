from flask import Flask, jsonify, render_template, request

from chatbot import FAQChatbot

app = Flask(__name__)
chatbot = FAQChatbot("data/faqs.json", confidence_threshold=0.35)


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/chat")
def chat():
    try:
        payload = request.get_json(silent=True)
        if not isinstance(payload, dict):
            return jsonify({
                "reply": "Please send a valid JSON request.",
                "status": "error"
            }), 400

        message = payload.get("message")
        if not isinstance(message, str) or not message.strip():
            return jsonify({
                "reply": "Please enter a question.",
                "status": "error"
            }), 400

        return jsonify(chatbot.get_response(message))
    except Exception:
        app.logger.exception("Chat request failed")
        return jsonify({
            "reply": "Something went wrong. Please try again.",
            "status": "error"
        }), 500


@app.errorhandler(404)
def not_found(_error):
    return jsonify({"reply": "The requested page could not be found.", "status": "error"}), 404


if __name__ == "__main__":
    app.run(debug=True)
