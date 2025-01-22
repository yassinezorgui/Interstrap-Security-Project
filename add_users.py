from app import db
from models import User
from werkzeug.security import generate_password_hash

#execute this script to add users to the database
while True:
    username = input("Enter username (or 'q' to quit): ")
    if username.lower() == 'q':
        break
    
    password = input("Enter password: ")
    email = input("Enter email: ")
    role = input("Enter role (user/admin): ")
    
    new_user = User(
        username=username,
        password=generate_password_hash(password),
        email=email,
        role=role
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        print(f"User {username} added successfully")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding user: {e}")