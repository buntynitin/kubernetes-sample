import os
from flask import Flask, request, jsonify
from publisher import producer
from flask_cors import CORS

# Init app
app = Flask(__name__)
CORS(app)


# Ping
@app.route('/', methods=['GET'])
def ping():
    return jsonify({"message": "Welcome to Mailer"}), 200


# Send a mail
@app.route('/mail', methods=['POST'])
def send_mail():
    try:
        producer.send(os.environ['TOPIC_NAME'], {
            "email": request.json['email'],
            "subject": request.json['subject'],
            "body": request.json['body'],
        })
        return jsonify({"message": "Your add request has been submitted"}), 200
    except():
        return jsonify({"error": "Something went wrong"}), 400


# Run Server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
