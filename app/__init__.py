from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

# Инициализация расширений
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.login'  # Указываем маршрут для страницы входа
login_manager.login_message_category = 'info'

from app.models import User  # Импорт модели User

# Функция для загрузки пользователя по ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Инициализация расширений с приложением
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Регистрация Blueprint (маршрутов)
    from app.routes import main
    app.register_blueprint(main)

    return app
