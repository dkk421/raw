from flask_login import UserMixin
from myapp import db, bcrypt, login_manager

ROLE_STUDENT = 0
ROLE_TEACHER = 1

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_STUDENT)

    def __repr__(self):
        return f'User({self.username},{self.email},{self.password},{self.role})'
















