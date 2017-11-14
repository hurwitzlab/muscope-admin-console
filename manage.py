#!/usr/bin/env python
import os

from flask_script import Manager

from app import create_app, db


app = create_app(os.environ.get('MUSCOPE_FLASK_CONFIG', default='development'))
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
