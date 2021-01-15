import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = '8<NP+2*@`1s+Mv?R{G]CAu-*!RqW9Q7X0wq3qFsOmB:~K]Qa#wG@z8&LlsZno'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:8889/rs-dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:8889/rs-test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:8889/rs-live'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
