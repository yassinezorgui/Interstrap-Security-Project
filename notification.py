from flask_mail import Mail, Message
from models import User, Task
from datetime import datetime, timedelta

mail = Mail()

def setup_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'zorguimohamedyassine@gmail.com'  
    app.config['MAIL_PASSWORD'] = 'ngxj cwbe vkff nkkk' 
    mail.init_app(app)

def send_task_notifications():
    """Send notifications for tasks due in the next 7 days"""
    from app import app
    with app.app_context():
        upcoming_tasks = Task.query.filter(
            Task.echeance_prochaine.between(
                datetime.now(),
                datetime.now() + timedelta(days=7)
            )
        ).all()
        
        if upcoming_tasks:
            users = User.query.all()
            for user in users:
                msg = Message(
                    'Upcoming Tasks Notification',
                    sender='zorguimohamedyassine@gmail.com',
                    recipients=[user.email]
                )
                
                task_list = "\n".join([
                    f"- {task.action_programmee} (Due: {task.echeance_prochaine.strftime('%Y-%m-%d')})"
                    for task in upcoming_tasks
                ])
                
                msg.body = f"""
                Hello {user.username},

                The following tasks are due in the next 7 days:

                {task_list}

                Best regards,
                Task Management System
                """
                
                mail.send(msg)