from flask import Flask, request, jsonify
# import os
import requests

app = Flask(__name__)

BOT_TOKEN = "BJAIE0CCEQHJEQYDFOATWSRHEJWBSONBYQWJMXNJYRHYULEGNMFEVKXGMGMPSGDK"


# def send_message(chat_id, text):
#     url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"
#     payload = {
#         "chat_id": chat_id,
#         "text": text,
#     }
#     response = requests.post(url, json=payload)
#     print("🔵 SendMessage Status:", response.status_code)
#     print("🔵 SendMessage Response:", response.text)
#     return response.json()


@app.route("/", methods=["GET"])
def index():
    return "✅ Rubika bot is running!", 200


@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.get_json()
    print("📩 پیام دریافتی از کاربر:")
    print(data)
    # try:
    #     text = data['inline_message']['text']
    #     sender = data['inline_message']['sender_id']
    #     print(f"👤 کاربر {sender} فرستاده: {text}")
    # except Exception as e:
    #     print("⚠️ مشکلی در خواندن پیام:", e)
    # return 'OK', 200

    # inline_msg = data.get("inline_message")
    # if inline_msg:
    #     chat_id = inline_msg.get("chat_id")
    #     text = inline_msg.get("text")
    #     send_message(chat_id, f"شما فرستادید: {text}")

    return "OK", 200


# @app.route("/receiveInlineMessage", methods=["POST"])
# def receive_inline():
#     data = request.get_json()
#     print("📩 receiveInlineMessage:", data)

#     update = data.get("update", {})
#     new_msg = update.get("new_message", {})
#     chat_id = update.get("chat_id")
#     text = new_msg.get("text")

#     if chat_id and text:
#         send_message(chat_id, f"✅ پیام شما دریافت شد: {text}")

#     return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(debug=True)
