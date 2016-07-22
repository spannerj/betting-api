from flask_log import Logging
import logging
from flask import g, ctx

# Create empty extension objects here
logger = Logging()


def register_extensions(app):
    """
    Adds any previously created extension objects into the app, and does any further setup they need.
    """
    # Logging
    logger.init_app(app)
    # Need to add the filter for trace id to both the werkzeug logger as well as the app logger, as
    # the native flask app server uses the werkzeug logger but gunicorn does not
    logging.getLogger('werkzeug').addFilter(ContextualFilter())
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
        if ctx.has_app_context():
            log_record.trace_id = g.trace_id
        else:
            log_record.trace_id = 'N/A'
        return True
