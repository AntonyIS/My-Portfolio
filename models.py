from app import *
db = SQLAlchemy(app)
from datetime import datetime


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    about = db.Column(db.String(50),nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    project = db.relationship('Project', backref='user', lazy=True)
    technical_experience = db.Column(db.Text, nullable=True)
    current_job  = db.Column(db.Text, nullable=True)
    educational_background   = db.Column(db.Text, nullable=True)
    profession   = db.Column(db.Text, nullable=True)
    python = db.Column(db.Text, nullable=True)
    javascript = db.Column(db.Text, nullable=True)
    java = db.Column(db.Text, nullable=True)
    django = db.Column(db.Text, nullable=True)
    flask = db.Column(db.Text, nullable=True)
    nodejs = db.Column(db.Text, nullable=True)
    android = db.Column(db.Text, nullable=True)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='project.jpg')
    user_id = db.Column(db.ForeignKey(User.id))
    # backend_language

    def __repr__(self):
        return  "User :{}".format(self.name)



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id =db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
