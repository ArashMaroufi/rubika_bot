import requests

token = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"

url = f'https://botapi.rubika.ir/v3/{token}/getMe'

response = requests.post(url)

print(response.text)
