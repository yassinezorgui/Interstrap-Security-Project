from flask import Flask
from flask_login import LoginManager
from models import db, User
from werkzeug.security import generate_password_hash
from config import Config
from notification import setup_mail
from scheduler import init_scheduler

def create_app():
    """Application factory function"""
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    init_scheduler(app)
    setup_mail(app)
    
    # Setup Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Create database tables and register routes
    with app.app_context():
        # Import and register routes
        from routes import register_routes
        register_routes(app)
        
        # Create database tables
        db.create_all()
        
        # Create admin user if it doesn't exist
        if not User.query.filter_by(username='admin').first():
            admin_user = User(
                username='admin',
                password=generate_password_hash('admin_password'),
                role='admin',
                email='yassine16kata@gmail.com',
            )
            db.session.add(admin_user)
            db.session.commit()
    
    return app

# Create the application instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)