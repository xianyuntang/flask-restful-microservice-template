from flask import Flask

from config.dev_config import DevConfig
from extensions import db, api, cors, migrate, ma
from extensions.router_extension import router_register

config_factory = {
    'dev': DevConfig
}


def create_app(config_name='dev'):
    app = Flask(__name__)

    app.config.from_object(config_factory[config_name])
    db.init_app(app)
    api.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    router_register(app)

    return app
