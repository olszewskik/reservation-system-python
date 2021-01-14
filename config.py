import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = '8<NP+2*@`1s+Mv?R{G]CAu-*!RqW9Q7X0wq3qFsOmB:~K]Qa#wG@z8&LlsZno'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
