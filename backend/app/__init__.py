from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from app.routes import api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    return app