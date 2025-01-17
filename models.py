from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model for authentication and authorization"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)

class Task(db.Model):
    """Task model for storing calendar tasks"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    volet = db.Column(db.String(100), nullable=False)
    action_programmee = db.Column(db.String(200), nullable=False)
    periodicite = db.Column(db.String(50), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    echeance_prochaine = db.Column(db.String(100), nullable=False)
    acteurs_externes = db.Column(db.String(200), nullable=True)