import os


class Configuration(object):
    """Config Class """
    DEBUG = False
    SECRET = os.getenv('SECRET')
    CSRF_ENABLED = True


class DevelopmentConfiguration(Configuration):
    """For Dev"""
    DEBUG = True


class TestingConfiguration(Configuration):
    """Test Configuration"""
    TESTING = True
    DEBUG = True


class ProductionConfiguration(Configuration):
    """For Production Stage"""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
}
