import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 60  # should be less than DB connection timeout
    SQLALCHEMY_DATABASE_URI = os.environ.get('MUSCOPE_DB_URI')

    SECRET_KEY = os.environ.get('MUSCOPE_ADMIN_CONSOLE_SESSION_SECRET_KEY')

    BASIC_AUTH_USERNAME = os.environ.get('MUSCOPE_ADMIN_CONSOLE_UN')  #'imicrobe-admin'
    BASIC_AUTH_PASSWORD = os.environ.get('MUSCOPE_ADMIN_CONSOLE_PW')
    BASIC_AUTH_FORCE = True

    def init_app(self, app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


configs = {
    'development': DevelopmentConfig(),
    'testing': TestingConfig(),
    'production': ProductionConfig()
}
