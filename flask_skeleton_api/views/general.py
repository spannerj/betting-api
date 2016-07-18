from flask import request, Blueprint
from flask_skeleton_api.app import app
import json

general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return json.dumps({
        "Status": "OK",
        "headers": str(request.headers),
        "commit": app.config["COMMIT"]
    })
