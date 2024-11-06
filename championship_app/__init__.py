from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Регистрация маршрутов
    from app.views.admin_routes import admin_bp
    from app.views.user_routes import user_bp
    from app.views.auth_routes import auth_bp

    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
