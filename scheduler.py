from flask_apscheduler import APScheduler
from notification import send_task_notifications

scheduler = APScheduler()

def init_scheduler(app):
    if not scheduler.running:
        scheduler.init_app(app)
        scheduler.add_job(id='task_notifications', 
                        func=send_task_notifications,
                        trigger='cron', 
                        hour=8,  
                        minute=50) # Send at 8:50 AM
        scheduler.start()