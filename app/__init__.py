from flask import Flask, render_template,send_file,send_from_directory
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, logout_user, login_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message, Mail
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config.from_object(Config)
db= SQLAlchemy(app)
migrate= Migrate(app, db)



mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'antonyshikubu@gmail.com',
    "MAIL_PASSWORD": 'GEOgraphy001'
}

app.config.update(mail_settings)
mail = Mail(app)

# setting login credentials
log_manager = LoginManager()
log_manager.login_view = 'login'
log_manager.init_app(app)

from app import views
from app  import models

#
#
#
