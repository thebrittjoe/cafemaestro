import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    # Flask security config
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha256'
    SECURITY_PASSWORD_SALT = 'test'
    SECURITY_SER_IDENTITY_ATTRIBUTES = ["username", "email"]

    # Flask security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_EMAIL_SENDER = os.environ.get('SECURITY_EMAIL_SENDER') or \
        'testmsecurity@gmail.com'
    # Flask securty URLs, overridden as they dont put a / at the end
    SECURITY_LOGIN_URL = '/login/'
    SECURITY_LOGOUT_URL = '/logout/'
    SECURITY_REGISTER_URL = '/register/'
    SECURITY_CHANGE_URL = '/change/'
    SECURITY_RESET_URL = '/reset/'
