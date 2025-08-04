from flask import Flask, request

app = Flask(__name__)


@app.route('/receiveUpdate', methods=['POST'])
def receive_update():
    data = request.json
    print("📩 Message received:", data)
    return "OK", 200


@app.route('/')
def home():
    return "Rubika bot is running!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
