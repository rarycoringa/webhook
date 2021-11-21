from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    response = {'greeting': 'Hello, Webhook!'}
    return jsonify(response), 200
