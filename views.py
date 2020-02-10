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
    return render_template('index_1.html', title='Antony Injila | Home')

@app.route('/404', methods=['POST', 'GET'])
def feedback():
    return render_template('feedback.html', title='Antony Injila | 404')

# user authentication
@app.route('/signup', methods=['POST','GET'])
def signup():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # check user exists
        if db.session.query(User).filter(User.email == email).count() > 0:
            error = "User exists!! Login"
            return render_template('signup.html', error=error)
        newUser = User(name=name,email=email,password=password)
        db.session.add(newUser)
        db.session.commit()
        flash("Signup successful.Login",'alert alert-success')
        return render_template('login.html')
    return render_template('signup.html', title="Antony Injila | Signup", error=error)


@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'antonyshikubu@gmail.com':
            error = 'Invalid email'
        elif request.form['password'] != 'pass1234':
            error = 'Invalid password'
        else:
            user = User.query.get(1)
            login_user(user)
            flash('Logging in was successful','altert alert-success')
            return redirect(url_for('index'))
    return render_template('login.html', title='Antony Injila | Login', error=error)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logout successful', 'alert alert-success')
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
@app.route('/projects/add', methods=['GET', 'POST'])
def projects_add():
    print(app.root_path)
    if request.method == 'POST':
        name  = request.form['name']
        description  = request.form['description']
        github  = request.form['github']
        youtube  = request.form['youtube']


        # grab imge file
        f = request.files['image-file']
        filename = secure_filename(f.filename)
        # location for storing images: Portfolio/static/images/name_of_image
        image_file = "{}/{}/{}".format("static", "images/uploads/projects", filename)
        # image upload
        f.save(os.path.join(UPLOAD_FOLDER + "/uploads/projects", filename))
        new_project = Project(
            name=name,
            description =description,
            github = github,
            youtube = youtube,
            image_file = image_file
        )
        db.session.add(new_project)
        db.session.commit()
        flash('{} added successfuly'.format(name), 'alert alert-success')
        return redirect(url_for('projects'))
    return render_template('projects.html', title='Antony Injila | Projects Add')


@app.route('/projects')
def projects():
    error = None
    projects = Project.query.all()
    print(projects)
    return render_template('projects.html', title = 'Antony Injila | Projects', projects=projects)


@app.route('/projects/detail/<int:project_id>')
def projects_detail(project_id):
    project = Project.query.get(project_id)
    print(project.image_file)
    return render_template('projects_detail.html', project=project)


@app.route('/projects/update/<int:project_id>')
def projects_update(project_id):
    return render_template('projects_update.html')


@app.route('/projects/delete/<int:project_id>')
def projects_delete(project_id):
    return render_template('projects.html')


