from flask import Response, current_app
import json


def unhandled_exception(e):
    import pdb; pdb.set_trace()
    current_app.logger.exception('Unhandled Exception: %s', repr(e), exc_info=True)
    return Response(response=json.dumps({"message": "Unexpected error."}), status=500)


def register_exception_handlers(app):
    app.register_error_handler(Exception, unhandled_exception)

    app.logger.info("Exception handlers registered")
