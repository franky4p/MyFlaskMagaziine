class Config(object):
    DEBAG = False
    TESTING = False
    DATABASE_URL = 'sqlite://memory'


class ProductionConfig(Config):
    DATABASE_URL = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBAG = True


