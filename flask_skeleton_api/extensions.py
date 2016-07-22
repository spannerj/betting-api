from flask_log import Logging
import logging
from flask.globals import _app_ctx_stack

# Create empty extension objects here
logger = Logging()


def register_extensions(app):
    """
    Adds any previously created extension objects into the app, and does any further setup they need.
    """
    # Logging
    logger.init_app(app)
    app.logger.addFilter(ContextualFilter())
    logger.set_formatter('%(asctime)s level=[%(levelname)s] traceid=[%(trace_id)s]' +
                         ' message=[%(message)s] exception=[%(exc_info)s]')

    # Using SQLAlchemy? An example can be found at 
    # http://192.168.249.38/gadgets/gadget-api/blob/master/gadget_api/extensions.py

    # All done!
    app.logger.info("Extensions registered")


class ContextualFilter(logging.Filter):
    def filter(self, log_record):
        """ Provide some extra variables to be placed into the log message """

        # If we have an app context (because we're servicing an http request) then get the trace id we have
        # set in g (see app.py)
        if _app_ctx_stack.top is not None:
            from flask import g
            log_record.trace_id = g.trace_id
        else:
            log_record.trace_id = 'N/A'
        return True
