import os
from flask_mail import Mail, Message

base_dir = os.path.abspath(os.path.dirname(__file__))
from datetime import datetime


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'topsecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(base_dir+'/app/static/images/uploads')



    MAIL_SERVER= 'smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='antonyshikubu@gmail.com',
    MAIL_PASSWORD='GEOgraphy001'




    ENV = 'prod'

    if ENV == 'dev':
        debug = True
        SQLALCHEMY_DATABASE_URI = "postgresql://antony:pass1234@localhost/portfolio"

    else:
        debug = False
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'postgres://atfiyllyjcgubb:2f87b57a08772fddad09ce5b3e21f00ac6814456cc2e98ca41eff6779fc9b90d@ec2-174-129-254-218.compute-1.amazonaws.com:5432/d826ivefni50d0'

