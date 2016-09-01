from flask_logconfig import LogConfig
import logging
import json
import traceback
import time
from flask import g, ctx
import collections

# Create empty extension objects here
logger = LogConfig()


def register_extensions(app):
    """
    Adds any previously created extension objects into the app, and does any further setup they need.
    """
    # Logging
    logger.init_app(app)

    # Along with the default flask logger (app.logger) define a new one specifically for audit. To use this logger
    # just add app.audit_logger.info("an audit point").
    app.audit_logger = logging.getLogger("audit")

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


class JsonFormatter(logging.Formatter):
    def format(self, record):
        if record.exc_info:
            exc = traceback.format_exception(*record.exc_info)
        else:
            exc = None

        log_entry = collections.OrderedDict()
        log_entry['timestamp'] = time.ctime(int(record.created)),
        log_entry['level'] = record.levelname,
        log_entry['traceid'] = record.trace_id,
        log_entry['message'] = record.msg % record.args,
        log_entry['exception'] = exc

        return json.dumps(log_entry)


class JsonAuditFormatter(logging.Formatter):
    def format(self, record):
        log_entry = collections.OrderedDict()
        log_entry['timestamp'] = time.ctime(int(record.created)),
        log_entry['level'] = 'AUDIT',
        log_entry['traceid'] = record.trace_id,
        log_entry['message'] = record.msg % record.args

        return json.dumps(log_entry)
