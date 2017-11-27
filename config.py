import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 60  # should be less than DB connection timeout
    SQLALCHEMY_DATABASE_URI = os.environ.get('MUSCOPE_DB_URI')

    SECRET_KEY = os.environ.get('MUSCOPE_ADMIN_CONSOLE_SESSION_SECRET_KEY')

    BASIC_AUTH_USERNAME = os.environ.get('MUSCOPE_ADMIN_CONSOLE_UN')
    BASIC_AUTH_PASSWORD = os.environ.get('MUSCOPE_ADMIN_CONSOLE_PW')
    BASIC_AUTH_FORCE = True

    def init_app(self, app):
        app.ADMIN_URL = self.ADMIN_URL
        print(self.BASIC_AUTH_USERNAME)
        print(self.BASIC_AUTH_PASSWORD)


class DevelopmentConfig(Config):
    DEBUG = True
    # this url can coexist with /imicrobe/admin on a development server
    ADMIN_URL = '/muscope/admin'


class ProductionConfig(Config):
    DEBUG = False
    ADMIN_URL = '/admin'


configs = {
    'development': DevelopmentConfig(),
    'production': ProductionConfig()
}
