from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_skeleton_api.models import *    # noqa
from flask_skeleton_api.app import app
from flask_skeleton_api.extensions import register_extensions, db

register_extensions(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
