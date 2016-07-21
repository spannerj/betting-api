from flask import request, Blueprint, Response
from flask_skeleton_api.app import app
import json
from flask import g

# This is the blueprint object that gets registered into the app in blueprints.py.
general = Blueprint('general', __name__)


@general.route("/health")
def check_status():
    return Response(response=json.dumps({
        "Status": "OK",
        "headers": str(request.headers),
        "commit": app.config["COMMIT"]
    }),  mimetype='application/json', status=200)


