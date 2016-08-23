# flask-skeleton

This repository contains a flask application structured in the way that all
Land Registry flask APIs should be structured going forwards.

You can use this to create your own app.
Take a copy of all the files, and change all occurences of flask-skeleton-api/flask_skeleton_api to your app name. There will be other places to tweak too such as the exposed port in docker-compose-fragment, so please look through every file before starting to extend it for your own use.

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

## Unit tests

[Pytest](http://docs.pytest.org/en/latest/) is used for unit testing. To run the tests run the following command:

```
py.test
```

The tests are automatically configured to run coverage and output to HTML.

## Notes

* This app contains the files necessary for Universal Dev Env support. See the [UDE readme](http://192.168.249.38/common/dev-env#tab-readme) for more info.
