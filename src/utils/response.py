from flask import jsonify
from flask import make_response as mr


class HttpStatus:
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500


def make_response(success, data, status_code):
    if success:
        response = data
    else:
        response = {
            'messages': data,
        }

    return mr(jsonify(response), status_code)
