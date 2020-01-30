from app import *
from models import User, Project,Comment,db
from werkzeug.utils import secure_filename
import os


@app.route('/')
def index():
    return render_template('index.html')


# user authentication
@app.route('/signup', methods=['POST','GET'])
def signup():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # check user exists
        if db.session.query(User).filter(User.email == email).count() > 0:
            message = "User with the email exists, try again"
            return redirect('signup')
        newUser = User(name=name,email=email,password=password)
        db.session.add(newUser)
        db.session.commit()
        message = "Signup successful"
        return render_template('login.html', message=message)
    return render_template('signup.html', title="Home")


@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # check user exists
        if db.session.query(User).filter(User.email == email).count() > 0:
            message = "User with the email exists, try again"
            return redirect(url_for('index'))
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


