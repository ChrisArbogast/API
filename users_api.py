from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "user 1"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)