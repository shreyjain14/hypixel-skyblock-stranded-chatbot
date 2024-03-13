from flask import Flask
from os import path, getenv
from dotenv import load_dotenv

load_dotenv('/.env')


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
