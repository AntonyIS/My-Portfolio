from flask import (Flask, render_template,url_for, request,redirect,flash)
from flask_login import login_user, logout_user, login_required,LoginManager, UserMixin,current_user
from datetime import datetime

import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

SECRET_KEY = os.urandom(24)
app.config['SECRET_KEY'] =SECRET_KEY
ENV = 'prod'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://antony:pass1234@localhost/Portfolio'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://atfiyllyjcgubb:2f87b57a08772fddad09ce5b3e21f00ac6814456cc2e98ca41eff6779fc9b90d@ec2-174-129-254-218.compute-1.amazonaws.com:5432/d826ivefni50d0'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "/Porfolio/static/images"

from views import *


if __name__ == '__main__':
    app.run()
