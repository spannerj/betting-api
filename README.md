# flask-skeleton

This repository contains a flask application structured in the way that all
Land Registry flask APIs should be structured going forwards.

## Quick start

```shell
# For Flask CLI
export FLASK_APP=flask_skeleton_api/main.py
export FLASK_DEBUG=1
# For Python
export PYTHONUNBUFFERED=yes
# For gunicorn
export PORT=9999
# For app's config.py
export FLASK_LOG_LEVEL=DEBUG
export COMMIT=LOCAL

# Run the app
flask run
```

## Notes

* This app contains the files necessary for Universal Dev Env support. See the [UDE readme](http://192.168.249.38/common/dev-env#tab-readme) for more info.


