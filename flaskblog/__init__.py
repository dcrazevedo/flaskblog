from flask import Flask
from flaskblog.config import Config
from flaskblog.ext.configuration import load_extensions


def create_app(config_clas=Config):

    app = Flask(__name__)
    app.config.from_object(Config)
    load_extensions(app)

    return app