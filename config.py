import os

class Config:
    SECRET_KEY = 'tu_clave_secreta'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(basedir, "instance", "tienda.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

