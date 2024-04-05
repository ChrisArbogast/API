from flask import Flask, Blueprint, jsonify, request

app2 = Blueprint('app2', __name__)

users = {
    "christian": {"password": "passworddata", "data": "ChristianData", "expiration": "2024-12-31"}
}

@app2.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]['password'] == password: expiration_date = users[username]['expiration']
    if expiration_date >= "2024-04-04":
        user_data = users[username]['data']
        return jsonify({"status": "success", "data": user_data})
    else: 
        return jsonify({"status": "error", "message": "Login Expired"})

if __name__ == '__main__':
    app2.run(debug=True)