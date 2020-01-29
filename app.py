from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# user authentication
@app.route('/signup')
def signup():
    return render_template('signup.html')


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
def projects(project_id):
    return render_template('projects_detail.html')


@app.route('/projects/update/<int:project_id>')
def projects_update(project_id):
    return render_template('projects_update.html')


@app.route('/projects/delete/<int:project_id>')
def projects_delete(project_id):
    return render_template('projects.html')




if __name__ == '__main__':
    app.run()
