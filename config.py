import os
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()


class Config:
    # Основные настройки Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'SportIsLife')
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'

    # Настройки базы данных PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Отключение отслеживания изменений для повышения производительности

    # Настройки для миграций базы данных
    MIGRATIONS_DIRECTORY = 'migrations'  # Папка для хранения миграций

    # Настройки сессий пользователей
    SESSION_COOKIE_SECURE = True  # Для безопасной передачи cookie (рекомендуется включить для HTTPS)
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 30  # Длительность "запомнить меня" (30 дней)

    # Настройки для загрузки файлов (например, аватары команд)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', 'championship_app/static/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Максимальный размер загружаемых файлов (16 МБ)

    # Настройки отправки почты (например, для подтверждения аккаунтов или восстановления пароля)
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.getenv('MAIL_PORT', 587)
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')
