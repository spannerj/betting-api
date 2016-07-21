from flask_log import Logging

# Create empty extension objects here
logger = Logging()


def register_extensions(app):
    """
    Adds any previously created extension objects into the app, and does any further setup they need.
    """
    # Logging
    logger.init_app(app)
    logger.set_formatter('%(asctime)s level=[%(levelname)s] logger=[%(name)s]' +
                         ' message=[%(message)s] exception=[%(exc_info)s]')

    # Using SQLAlchemy? An example can be found at 
    # http://192.168.249.38/gadgets/gadget-api/blob/master/gadget_api/extensions.py

    # All done!
    app.logger.info("Extensions registered")
