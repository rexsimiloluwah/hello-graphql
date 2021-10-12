from flask import Flask

def init_app():
    app = Flask(__name__)

    @app.route("/")
    def hello() -> str:
        return "Hello World, We are under construction."
    
    return app