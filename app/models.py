from flask_security import UserMixin, RoleMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RolesUsers(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer, db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(65), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255), index=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    roles = db.relationship('Roles', secondary='roles_users', 
                            backref=db.backref('user', lazy='dynamic'))
