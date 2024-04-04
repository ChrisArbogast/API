from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "title": "book 1", "author": "author 1"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)