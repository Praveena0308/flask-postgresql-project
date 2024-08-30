import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://flask_user:1234@localhost:5432/flask_db?sslmode=disable')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
