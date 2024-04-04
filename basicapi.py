from flask import flask
from books_api import app as books_app
from user_api import app as users_app

app = Flask(__name__)

app.register_blueprint(books_app)
app.register_blueprint(users_app)

if __name__ == '__main__':
    app.run(debug=True)