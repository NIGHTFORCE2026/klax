#!/usr/bin/env python

# LAUNCH SCRIPT TO START THE APPLICATION
import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

# create the application instance
app = create_app(os.environ.get('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

# add shell context for manager and migrate
def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# unit test launcher
@manager.command
def test():
    """ Run the unit tests. """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
