


from flask import Flask
from routes import register_routes
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    register_routes(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
