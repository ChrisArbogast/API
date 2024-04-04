from flask import Flask, Blueprint, jsonify

test2_app = Blueprint('test2_app', __name__)

test2 = [
    {"id": 1, "test2": "test2"}
]

@test2_app.route('/test2', methods=['GET'])
def get_test2():
    return jsonify(test2)

if __name__ == '__main__':
    app.run(debug=True)