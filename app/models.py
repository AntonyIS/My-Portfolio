from app import *



class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    password= db.Column(db.String(300),nullable=False)
    about = db.Column(db.String(500),nullable=True)
    image_file = db.Column(db.String(120), nullable=True, default='default.jpg')
    cv_file = db.Column(db.String(120), nullable=True, default='default.jpg')
    technical_experience = db.Column(db.Text, nullable=True)
    current_job = db.Column(db.Text, nullable=True)
    educational_background = db.Column(db.Text, nullable=True)
    profession = db.Column(db.Text, nullable=True)
    recent_activities = db.Column(db.Text, nullable=True)
    python = db.Column(db.Text, nullable=True)
    javascript = db.Column(db.Text, nullable=True)
    java = db.Column(db.Text, nullable=True)
    django = db.Column(db.Text, nullable=True)
    flask = db.Column(db.Text, nullable=True)
    nodejs = db.Column(db.Text, nullable=True)
    android = db.Column(db.Text, nullable=True)
    projects = db.relationship('Project', backref='user', lazy='dynamic')

    def __repr__(self):
        return "User :{}".format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    github = db.Column(db.String(200), nullable=False)
    youtube = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='project.jpg')
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    technologies = db.Column(db.String(200), nullable=True, default='Python')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))



    def __repr__(self):
        return  "Project :{}".format(self.name)


class Comment(db.Model):
    __tablename__ ="comments"
    id = db.Column(db.Integer, primary_key=True)
    project_id =db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow()) 