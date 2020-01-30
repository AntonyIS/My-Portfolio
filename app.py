from flask import Flask, render_template, request
import os
from flask_login import login_user, logout_user, login_required,LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://antony:pass1234@localhost/Signup'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://weecywyhmtjnvd:1a75f2ed2f8d8cd557420b1ec6d11bb7c896cb27d76c2e48f5e6e35201498961@ec2-52-203-98-126.compute-1.amazonaws.com:5432/d8ndro69ratulc'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SECRET_KEY = os.urandom(24)

SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ "/Portfolio/static/images"


@app.route('/')
def index():
    return render_template('index.html')


# user authentication
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['username']

        # check user exists
        print(username,email,password)
    return render_template('signup.html', title="Home")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/about')
def about():
    return render_template('about.html')

# Projects urls and views
@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/projects/detail/<int:project_id>')
def projects_detail(project_id):
    return render_template('projects_detail.html')


@app.route('/projects/update/<int:project_id>')
def projects_update(project_id):
    return render_template('projects_update.html')


@app.route('/projects/delete/<int:project_id>')
def projects_delete(project_id):
    return render_template('projects.html')




if __name__ == '__main__':
    app.run()
