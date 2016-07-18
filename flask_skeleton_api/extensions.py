from flask_log import Logging

logger = Logging()


def register_extensions(app):
    logger.init_app(app)
    logger.set_formatter('%(asctime)s level=[%(levelname)s] logger=[%(name)s]' +
                         ' message=[%(message)s] exception=[%(exc_info)s]')

    app.logger.info("Extensions registered")
