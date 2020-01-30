from flask import (Flask, render_template,url_for, request,redirect,flash)
from flask_login import login_user, logout_user, login_required,LoginManager, UserMixin
from datetime import datetime

import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
ENV = 'dev'

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

SECRET_KEY = os.urandom(24)
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://antony:pass1234@localhost/Portfolio'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] =''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "/Portfolio/static/images"

from views import *


if __name__ == '__main__':
    app.run()
