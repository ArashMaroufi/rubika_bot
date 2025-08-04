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
    print("🔵 SendMessage Status:", response.status_code)
    print("🔵 SendMessage Response:", response.text)


@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.json
    print("📩 Received data:", data)

    if not data:
        print("⚠️ Warning: Received empty JSON!")
        return "No data", 400

    # سعی می‌کنیم chat_id و متن پیام رو استخراج کنیم
    message = data.get("message")
    if not message:
        print("⚠️ Warning: 'message' field missing in data!")
        return "No message field", 400

    chat_id = message.get("chat_id")
    text = message.get("text")

    print(f"➡️ chat_id: {chat_id}")
    print(f"➡️ text: {text}")

    if chat_id and text:
        reply_text = f"پیام شما: {text}"
        send_message(chat_id, reply_text)
    else:
        print("⚠️ chat_id یا text موجود نیست!")

    return "OK", 200


@app.route('/')
def home():
    return "Rubika bot is running!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
