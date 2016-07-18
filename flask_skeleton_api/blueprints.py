from flask_skeleton_api.views import general


def register_blueprints(app):
    app.register_blueprint(general.general)

    app.logger.info("Blueprints registered")
