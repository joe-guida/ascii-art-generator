from decouple import config

class Config(object):

    class DebugConfig:
        DEBUG = True
        DEVELOPMENT = True
        SECRET_KEY=config('SECRET_KEY')
        TEMPLATES_AUTO_RELOAD = True

    class ProductionConfig:
        pass