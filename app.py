


from flask import Flask
from routes import register_routes
from extensions import db, ma
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"{os.getenv('DATABASE_SCHEME')}{os.getenv('DATABASE_USER')}@"
        f"{os.getenv('DATABASE_ADDRESS')}:{os.getenv('DATABASE_PORT')}/"
        f"{os.getenv('DATABASE_NAME')}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    ma.init_app(app)

    register_routes(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host=os.getenv('FLASK_HOST'), port=int(os.getenv('FLASK_PORT')), debug=True)
