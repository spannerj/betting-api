from flask import Response, current_app
import json


def unhandled_exception(e):
    current_app.logger.exception('Unhandled Exception: %s', repr(e))
    return Response(response=json.dumps({"message": "Unexpected error.", "error_code": "001"}), status=500)


def register_exception_handlers(app):
    app.register_error_handler(Exception, unhandled_exception)

    app.logger.info("Exception handlers registered")
