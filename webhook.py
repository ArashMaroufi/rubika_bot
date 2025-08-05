import requests

BOT_TOKEN = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"
WEBHOOK_URL = "https://rubika-bot-spz2.onrender.com/receiveUpdate"

# url = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateEndpoint'

data = {
    "url": WEBHOOK_URL,
    "type": "GetSelectionItem"
}
url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateBotEndpoints"

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)
