from flask_skeleton_api.app import app
from flask_skeleton_api.extensions import register_extensions
from flask_skeleton_api.blueprints import register_blueprints

register_extensions(app)
register_blueprints(app)
