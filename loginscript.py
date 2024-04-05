from flask import request, jsonify
url = 'http://127.0.0.1:5000/login'

login_data = {
    'username': 'christian',
    'password': 'passworddata'
}

response = request.post(url, json=login_data)

print(response.json())