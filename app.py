from flask import Flask
from extensions import db
from config import config_factory
from extensions.router_extension import router_register


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_factory[config_name])

    db.init_app(app)

    router_register(app)

    return app
