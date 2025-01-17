# Create a new file called reset_db.py
from app import create_app
from models import db

app = create_app()

with app.app_context():
    # Drop all tables
    db.drop_all()
    
    # Create all tables with new schema
    db.create_all()
    
    print("Database reset successfully!")