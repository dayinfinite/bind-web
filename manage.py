#!/usr/bin/env python
# coding=utf-8


import os
from service import create_app, db
from flask_sctipt import Manager, Shell
from flask_migrate import Migrate, Migrate_Command

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
