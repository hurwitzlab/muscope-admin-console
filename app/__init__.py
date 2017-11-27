import os

from flask import Flask
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

from config import configs


db = SQLAlchemy()

from app import models
from app.model_view import MuScopeModelView


def create_app(config_name):
    app_ = Flask(__name__)

    app_.config.from_object(configs[config_name])

    configs[config_name].init_app(app_)

    basic_auth = BasicAuth(app_)

    db.init_app(app_)

    admin = Admin(
        app_,
        name='muSCOPE Administration Console',
        template_mode='bootstrap3',
        url=app_.ADMIN_URL)

    print(app_.ADMIN_URL)

    for models_class in models.__dict__.values():
        if isinstance(models_class, type) and models_class.__module__ == models.__name__:
            view = MuScopeModelView(models_class, db.session)
            admin.add_view(view)
        else:
            pass
            #print('"{}" is not a database model'.format(models_class))

    return app_
