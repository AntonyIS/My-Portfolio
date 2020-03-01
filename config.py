import os
from flask_mail import Mail, Message

base_dir = os.path.abspath(os.path.dirname(__file__))
from datetime import datetime


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'topsecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(base_dir+'/app/static/images/uploads')
