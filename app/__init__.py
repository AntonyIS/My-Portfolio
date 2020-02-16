from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, logout_user
from datetime import datetime
from .models import User
# from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db= SQLAlchemy(app)
# migrate= Migrate(app, db)



# setting login credentials
log_manager = LoginManager()
log_manager.login_view = 'login'
log_manager.init_app(app)


@log_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

from app import views, models

