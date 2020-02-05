from app import *
from models import User, Project,Comment,db
from werkzeug.utils import secure_filename
import os

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index_1.html')

@app.route('/404', methods=['POST', 'GET'])
def feedback():
    return render_template('feedback.html', title='Antony Injila | 404')

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
    # if current_user.is_authenticated:
    #     return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # check user exists
        if email == 'antonyshikubu@gmail.com' and password == 'pass1234':
            user = User.query.get(1)
            login_user(user)
            return redirect(url_for('index'))
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route("/logout")

def logout():
    logout_user()
    flash('logout successful', 'alert alert-success')
    return redirect(url_for('index'))


@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    projects = Project.query.all()
    if request.form and request.files:
        name = request.form.get('name')
        email = request.form.get('email')
        about = request.form.get('about')

        f = request.files['image-file']
        filename = secure_filename(f.filename)
        # location for storing images: Portfolio/static/images/name_of_image
        image_file = "{}/{}/{}".format("static", "images/uploads", filename)
        # image upload
        f.save(os.path.join(app.config["UPLOAD_FOLDER"] + "/uploads", filename))

        user = User(name=name,email=email,about=about,image_file=image_file)
        db.session.add(user)
        db.session.commit()
        user = User.query.get(1)
        return render_template('dashboard.html',title="Antony Injila | Dashboard",user=user )
    user = User.query.get(1)
    count = len(projects)
    return render_template('dashboard.html', title="Antony Injila | Dashboard", user=user,count=count, projects=projects)


@app.route('/dashboard/update', methods=['GET','POST'])
def dashboard_update():
    projects = Project.query.all()
    user = User.query.get(1)
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        about = request.form.get('about')
        technical_experience = request.form.get('technical_experience')
        current_job = request.form.get('current_job')
        educational_background = request.form.get('educational_background')
        profession = request.form.get('profession')
        python = request.form.get('python')
        javascript = request.form.get('javascript')
        java = request.form.get('java')
        django = request.form.get('django')
        flask = request.form.get('flask')
        nodejs = request.form.get('nodejs')
        android = request.form.get('android')

        image_file_old = request.form.get('image-file-old')
        f = request.files['image-file']
        filename = secure_filename(f.filename)

        print()
        if filename:
            # location for storing images: Portfolio/static/images/name_of_image
            image_file = "{}/{}/{}".format("static", "images/uploads", filename)

            # image upload
            f.save(os.path.join(app.config["UPLOAD_FOLDER"] + "/uploads", filename))
            user.image_file = image_file
            db.session.commit()
        else:
            user.name = name
            user.email = email
            user.about = about
            user.technical_experience = technical_experience
            user.current_job = current_job
            user.educational_background = educational_background
            user.profession = profession
            user.python = python
            user.javascript = javascript
            user.java = java
            user.django = django
            user.flask = flask
            user.nodejs = nodejs
            user.android = android
            user.image_file = image_file_old

        # save the new changes
            db.session.commit()
        # return redirect('/project/update/{}/'.format(project_id))
            return redirect(url_for('dashboard'))

    return render_template('dashboard.html', title="Antony Injila | Dashboard update", user=user, projects=projects)

@app.route('/about')
def about():
    user = User.query.get(1)
    return render_template('about.html', title='Antony Injila | About page', user=user)

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


