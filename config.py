
class Config:
    SECRET_KEY = 'demo'
    SSL_DISABLE = False
    @staticmethod
    def init_app(app):
        pass

class Local(Config):
    DEBUG = True

class Development(Config):
    DEBUG = True

class Production(Config):
    pass

config = {
    'local': Local,
    'development': Development,
    'production': Production
}
