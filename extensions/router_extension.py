from src.routers import blueprint


def router_register(app):
    app.register_blueprint(blueprint)
