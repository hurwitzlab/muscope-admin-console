import os

from flask import Flask
from flask_admin import Admin
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy

from config import configs


db = SQLAlchemy()

from app import models
from app.model_view import MuScopeModelView, SampleView, SampleFileView


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

    for model_class in models.__dict__.values():
        if isinstance(model_class, type) and model_class.__module__ == models.__name__:
            print('found model class "{}"'.format(model_class.__name__))
            if model_class.__name__ == 'Sample':
                view = SampleView(model_class, db.session)
            elif model_class.__name__ == 'Sample_file':
                view = SampleFileView(model_class, db.session)
            else:
                view = MuScopeModelView(model_class, db.session)
            admin.add_view(view)
        else:
            pass

    return app_
