import requests
# import json

BOT_TOKEN = "BIABH0NLKZETIEBOCAMXQAEJEPAZMVMEPONHMEHNVXGHRPLRVJQTTAQECKNOKELX"
CHAT_ID = "b0Cz5Y50EqW0f547a653c9d0389433ed"

url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/getBotEndpoints"

response = requests.get(url)
print(response.status_code)
print(response.text)

# data = {
#     "chat_id": CHAT_ID,
#     "question": "Do you have any question?",
#     "options": ["yes", "no"],
# }

# response = requests.post(url, json=data)

# print(response.text)


# data = {
#     "chat_id": CHAT_ID,
#     "text": "Welcome",
#     "chat_keypad_type": "New",
#     "chat_keypad": {
#         "rows": [
#             {
#                 "buttons": [
#                     {
#                         "id": "100",
#                         "type": "Simple",
#                         "button_text": "Add Account"
#                     }
#                 ]
#             },
#             {
#                 "buttons": [
#                     {
#                         "id": "101",
#                         "type": "Simple",
#                         "button_text": "Edit Account"
#                     },
#                     {
#                         "id": "102",
#                         "type": "Simple",
#                         "button_text": "Remove Account"
#                     }
#                 ]
#             }
#         ],
#         "resize_keyboard": True,
#         "on_time_keyboard": False
#     }
# }
# headers = {
#     'Content-Type': 'application/json'
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)
