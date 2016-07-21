from flask import request, Blueprint
from flask_skeleton_api.app import app
import json

# This is the blueprint object that gets registered into the app in blueprints.py.
general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return json.dumps({
        "Status": "OK",
        "headers": str(request.headers),
        "commit": app.config["COMMIT"]
    })
