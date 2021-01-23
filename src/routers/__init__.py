from flask import Blueprint
from extensions import api

blueprint = Blueprint('account', __name__, url_prefix='/account')
api.add_resource()