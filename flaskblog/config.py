import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USENAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

class Extensions:
    DEFAULT = [
        'flaskblog.ext.database',
        'flaskblog.ext.encrypt', 
        'flaskblog.ext.login', 
        'flaskblog.ext.mail',
        'flaskblog.blueprints']
    DEVELOPMENT = [
        'flaskblog.ext.database',
        'flaskblog.ext.encrypt', 
        'flaskblog.ext.login', 
        'flaskblog.ext.mail',
        'flaskblog.blueprints']
    PRODUCTION = [
        'flaskblog.ext.database',
        'flaskblog.ext.encrypt', 
        'flaskblog.ext.login', 
        'flaskblog.ext.mail',
        'flaskblog.blueprints']