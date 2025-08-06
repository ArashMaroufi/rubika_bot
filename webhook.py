# import requests

# BOT_TOKEN = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"
# WEBHOOK_URL = "https://rubika-bot-spz2.onrender.com/receiveUpdate"

# # url = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateEndpoint'

# data = {
#     "url": WEBHOOK_URL,
#     "type": "GetSelectionItem"
# }
# url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateBotEndpoints"

# response = requests.post(url, json=data)

# print("Status Code:", response.status_code)
# print("Response:", response.text)
import requests

url = "https://rubika-bot-spz2.onrender.com/receiveUpdate"
# BOT_TOKEN = "BJAIE0CCEQHJEQYDFOATWSRHEJWBSONBYQWJMXNJYRHYULEGNMFEVKXGMGMPSGDK"
payload = {
    "inline_message": {
        "sender_id": "test-user",
        "text": "سلام",
        "location": None,
        "aux_data": {
            "start_id": None,
            "button_id": "test-btn"
        },
        "message_id": "1234567890",
        "chat_id": "chat-1234"
    }
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.text)
