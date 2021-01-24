from marshmallow import ValidationError

from src.utils.response import HttpStatus


class Logic:
    Manager = None
    Schema = None

    def __init__(self):
        if self.Manager is not None:
            self.manager = self.Manager()
        if self.Schema is not None:
            self.schema = self.Schema()

    def retrieve(self, pk):
        success, res = self.manager.retrieve(pk)

        if success:
            if res:
                return success, self.schema.dump(res, many=False), HttpStatus.OK
            else:
                return success, None, HttpStatus.NO_CONTENT

        else:
            return success, res, HttpStatus.BAD_REQUEST

    def list(self):
        success, res = self.manager.list()

        if success:
            if res:
                return success, self.schema.dump(res, many=True), HttpStatus.OK
            else:
                return success, None, HttpStatus.NO_CONTENT

        else:
            return success, res, HttpStatus.BAD_REQUEST

    def create(self, data):
        try:
            data = self.schema.load(data)
            success, res = self.manager.create(data)
            if success:
                return success, self.schema.dump(res), HttpStatus.CREATED
            else:
                return success, res, HttpStatus.INTERNAL_SERVER_ERROR
        except ValidationError as e:
            return False, e.messages, HttpStatus.BAD_REQUEST

    def delete(self, pk):
        success, res = self.manager.delete(pk)

        if success:
            return success, None, HttpStatus.NO_CONTENT
        else:
            return success, res, HttpStatus.NOT_FOUND
