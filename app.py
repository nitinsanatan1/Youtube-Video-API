from flask import Flask
app = Flask(__name__)

def initialize_app(testing: bool = False):
    @app.route("/")
    def home():
        return "Hello, Flask!"

    return app