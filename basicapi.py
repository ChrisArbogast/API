from flask import Flask
from test_api import test_app
from app import app2

app = Flask(__name__)

app.register_blueprint(test_app)
app.register_blueprint(app2)

if __name__ == '__main__':
    app.run(debug=True)