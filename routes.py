from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user
from werkzeug.security import check_password_hash
from models import User, Task, db
from forms import LoginForm, TaskForm
from datetime import datetime

def register_routes(app):
    """Register all routes with the Flask application"""
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('tasks_calendar'))  # Changed from add_task
            flash('Invalid username or password.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/add-task', methods=['GET', 'POST'])
    @login_required
    def add_task():
        """Handle task creation (admin only)"""
        if current_user.role != 'admin':
            flash('Access denied. Admins only.', 'danger')
            return redirect(url_for('login'))
            
        form = TaskForm()
        if form.validate_on_submit():
            task = Task(
                volet=form.volet.data,
                action_programmee=form.action_programmee.data,
                periodicite=form.periodicite.data,
                responsable=form.responsable.data,
                echeance_prochaine=form.echeance_prochaine.data,
                acteurs_externes=form.acteurs_externes.data
            )
            db.session.add(task)
            db.session.commit()
            flash('Task added successfully!', 'success')
            return redirect(url_for('add_task'))
        return render_template('add_task.html', form=form)
    
    @app.route('/calendar')
    @login_required
    def tasks_calendar():
        tasks = Task.query.order_by(Task.echeance_prochaine).all()
        return render_template('tasks_calendar.html', 
                             tasks=tasks,
                             today=datetime.now().date())
    
    @app.route('/complete-task/<int:task_id>', methods=['POST'])
    @login_required
    def complete_task(task_id):
        task = Task.query.get_or_404(task_id)
        task.complete_task()
        db.session.commit()
        flash('Task marked as complete and next due date updated!', 'success')
        return redirect(url_for('tasks_calendar'))

    @app.route('/')
    def home():
        """Redirect root URL to login page"""
        return redirect(url_for('login'))