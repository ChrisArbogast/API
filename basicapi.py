from flask import Flask
from test_api import test_app
from test2_api import test2_app

app = Flask(__name__)

app.register_blueprint(test_app)
app.register_blueprint(test2_app)

if __name__ == '__main__':
    app.run(debug=True)