from flask import Flask, request, jsonify
# import os
import requests
import logging

app = Flask(__name__)

BOT_TOKEN = "BJAIE0CCEQHJEQYDFOATWSRHEJWBSONBYQWJMXNJYRHYULEGNMFEVKXGMGMPSGDK"

logging.basicConfig(level=logging.INFO)


@app.route("/", methods=["GET"])
def index():
    return "✅ Rubika bot is running!", 200


@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    logging.info("🔔 درخواست POST دریافت شد")

    try:
        data = request.get_json(force=True)
        logging.info(f"📩 داده دریافتی:\n{data}")
    except Exception as e:
        logging.error("❌ خطا در خواندن JSON:")
        logging.error(e)

    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True)
