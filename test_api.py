from flask import Flask, Blueprint, jsonify

test_app = Blueprint('test_app', __name__)

test = [
    {"id": 1, "test": "testdata"}
]

@test_app.route('/test', methods=['GET'])
def get_test():
    return jsonify(test)

if __name__ == '__main__':
    app.run(debug=True)     