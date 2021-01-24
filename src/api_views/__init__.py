from flask import request
from flask_restful import Resource

from src.utils.response import make_response


class ApiView(Resource):
    Logic = None

    def __init__(self):
        if self.Logic is not None:
            self.logic = self.Logic()

    def get(self, pk=None):
        if pk is not None:
            success, data, status = self.logic.retrieve(pk)
        else:
            success, data, status = self.logic.list()
        return make_response(success, data, status)

    def post(self):
        json = request.get_json()
        success, data, status = self.logic.create(json)
        return make_response(success, data, status)

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self, pk):
        success, data, status = self.logic.delete(pk)
        return make_response(success, data, status)
