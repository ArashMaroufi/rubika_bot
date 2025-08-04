from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"


def send_message(chat_id, text):
    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=payload)
    print("SendMessage Status:", response.status_code)
    print("SendMessage Response:", response.text)


@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.json
    print("📩 Message received:", data)

    # استخراج chat_id و متن پیام
    message = data.get("message", {})
    chat_id = message.get("chat_id")
    text = message.get("text", "")

    if chat_id and text:
        reply_text = f"پیام شما: {text}"
        send_message(chat_id, reply_text)

    return "OK", 200


@app.route('/')
def home():
    return "Rubika bot is running!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
