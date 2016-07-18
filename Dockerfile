# Set the base image to the base image
FROM lr_base_python_flask

# ---- Uncomment the following lines if app will be using a postgres database
# RUN yum install -y -q postgresql-devel
# These must match the settings in the postgres Dockerfile:
# ENV SQL_HOST postgres
# ENV SQL_DATABASE skeletonapi
# ENV ALEMBIC_SQL_USERNAME root
# (This will be temporarily overidden to yes when the alembic database upgrade is run)
# ENV SQL_USE_ALEMBIC_USER no
# ----

# Port for gunicorn
# Default to 8080, docker-compose can change this to the reserved port for this app
ENV PORT 8080

# ----
# Put your app-specific stuff here (extra yum installs etc).
# Any environment variables your config.py needs should also be added as ENV entries here

# Set the log level to DEBUG for development
ENV FLASK_LOG_LEVEL DEBUG
# Set commit to be local for development
ENV COMMIT LOCAL


CMD ["/usr/local/bin/gunicorn", "-k", "eventlet", "--pythonpath", "/src", "--access-logfile", "-", "flask_skeleton_api.main:app", "--reload"]
# ----

# Get the python environment ready
# Have this at the end so if the files change, all the other steps
# don't need to be rerun. Same reason why _test is first.
# This ensures the container always has just what is in the requirements files as it will
# rerun this in a clean image.
ADD requirements_test.txt requirements_test.txt
ADD requirements.txt requirements.txt
RUN pip3 install -q -r requirements.txt && \
  pip3 install -q -r requirements_test.txt
