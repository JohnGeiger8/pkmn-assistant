from flask import Flask
from dotenv import load_dotenv

from app.config import Config


def create_app() -> Flask:
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app