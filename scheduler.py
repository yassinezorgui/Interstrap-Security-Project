from flask_apscheduler import APScheduler
from notification import send_task_notifications

scheduler = APScheduler()

def init_scheduler(app):
    scheduler.init_app(app)
    scheduler.add_job(id='task_notifications', 
                     func=send_task_notifications,
                     trigger='cron', 
                     hour=9,  # Send at 9 AM
                     minute=0)
    scheduler.start()