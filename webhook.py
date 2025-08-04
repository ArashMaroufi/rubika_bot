import requests

BOT_TOKEN = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"
WEBHOOK_URL = "https://rubika-bot-spz2.onrender.com/receiveUpdate"

url = f'https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateEndpoint'

payload = {
    "url": WEBHOOK_URL
}

response = requests.post(url, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)
