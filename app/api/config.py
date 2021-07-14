"""Flask Configuration"""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

FLASK_ENV = 'development'
TESTING = True
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/sistem_rapor_pweb'
SQLALCHEMY_TRACK_MODIFICATIONS = False