from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger

from src.api_views import api_view

blueprint = Blueprint('account', __name__, url_prefix='/account')
api = swagger.docs(Api(blueprint))
api.add_resource(api_view.User, '/users', '/users/<pk>')
