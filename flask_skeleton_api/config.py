import os
# RULES OF CONFIG:
# 1. No region specific code. Regions are defined by setting the OS environment variables appropriately to build up the
# desired behaviour.
# 2. No use of defaults when getting OS environment variables. They must all be set to the required values prior to the
# app starting.
# 3. This is the only file in the app where os.getenv should be used.

# For logging
FLASK_LOG_LEVEL = os.getenv('FLASK_LOG_LEVEL')
# For health route
COMMIT = os.getenv('COMMIT')

# Using SQLAlchemy/Postgres?
# The required variables (and required usage) can be found here:
# http://192.168.249.38/gadgets/gadget-api/blob/master/gadget_api/config.py


