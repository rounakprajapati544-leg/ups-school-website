from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend Running Successfully"

@app.route("/check_fee", methods=["POST"])
def check_fee():
    data = request.json

    return jsonify({
        "student": {"StudentName": "Demo Student"},
        "total_fee": 12000,
        "paid_fee": 7000,
        "pending_fee": 5000,
        "breakdown": [
            {"Month": "June", "Amount": 6000, "Status": "Paid"},
            {"Month": "July", "Amount": 6000, "Status": "Pending"}
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
