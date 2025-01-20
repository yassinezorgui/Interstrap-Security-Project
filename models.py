from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model for authentication and authorization"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  # Add email
    role = db.Column(db.String(10), nullable=False)

class Task(db.Model):
    """Task model for storing calendar tasks"""
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    volet = db.Column(db.String(100), nullable=False)
    action_programmee = db.Column(db.String(200), nullable=False)
    periodicite = db.Column(db.String(50), nullable=False)
    responsable = db.Column(db.String(100), nullable=False)
    echeance_prochaine = db.Column(db.DateTime, nullable=False)  # Changed from String to DateTime
    acteurs_externes = db.Column(db.String(200), nullable=True)
    last_completed = db.Column(db.DateTime, nullable=True)

    def calculate_next_due_date(self):
        """Calculate next due date based on periodicite"""
        amount, unit = self.periodicite.lower().split()
        amount = int(amount)
        
        today = datetime.now()
        
        if 'day' in unit:
            return today + timedelta(days=amount)
        elif 'week' in unit:
            return today + timedelta(weeks=amount)
        elif 'month' in unit:
            return today + relativedelta(months=amount)
        elif 'year' in unit or 'annual' in unit:
            return today + relativedelta(years=amount)
        
        return today
    
    def is_due_soon(self, days=7):
        """Check if task is due within specified days"""
        if not self.echeance_prochaine:
            return False
        return datetime.now() <= self.echeance_prochaine <= datetime.now() + timedelta(days=days)

    def complete_task(self):
        """Mark task as complete and calculate next due date"""
        self.last_completed = datetime.now()
        # Parse periodicite and add to current date
        amount, unit = self.periodicite.split()
        amount = int(amount)
        
        if 'day' in unit.lower():
            delta = timedelta(days=amount)
        elif 'week' in unit.lower():
            delta = timedelta(weeks=amount)
        elif 'month' in unit.lower():
            # Approximate months as 30 days
            delta = timedelta(days=amount * 30)
            
        self.echeance_prochaine = datetime.now() + delta