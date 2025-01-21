# Task Notification and Management System

This project is a **Task Notification and Management System** built using Flask, Flask-SQLAlchemy, and Flask-APScheduler. It allows users to manage tasks, send notifications for upcoming tasks via email, and visualize schedules effectively.

---

## Features

- **Task Management**: Create, update, and delete tasks.
- **Email Notifications**: Automatically sends email reminders for upcoming tasks.
- **Scheduling**: Uses APScheduler to schedule and manage periodic tasks.
- **Role-Based Access**: Login system with different user roles (e.g., admin, user).
- **Task Visualization**: View and filter tasks in a calendar or list format.
- **Customizable Configurations**: Easily configure notification times and email settings.

---

## Tech Stack

- **Backend**: Flask
- **Database**: Flask-SQLAlchemy (SQLite)
- **Scheduler**: Flask-APScheduler
- **Email Service**: Flask-Mail
- **Frontend**: HTML, CSS, JavaScript (with Flask templates)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yassinezorgui/Interstrap-Security-Project.git
   cd Interstrap-Security-Project
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the environment variables in at `notification.py` file:
   ```env
   def setup_mail(app):
       app.config['MAIL_SERVER'] = 'smtp.gmail.com'
       app.config['MAIL_PORT'] = 587
       app.config['MAIL_USE_TLS'] = True
       app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  
       app.config['MAIL_PASSWORD'] = 'your-email-password' 
       mail.init_app(app)
   ```

5. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Run the application:
   ```bash
   flask run
   ```

---

## Usage

### Task Notifications
The system sends email notifications for tasks that are due within the next 7 days. Notifications are handled using `Flask-APScheduler`.

### Adding a Task
Navigate to `/tasks` to create or manage tasks. Each task includes a title, description, and due date.

### Viewing Tasks
Tasks can be viewed in a calendar format. Filters are available to sort tasks by date, voley or priority.

---


## Troubleshooting

### Common Issues

1. **Working Outside Application Context**:
   Ensure the correct usage of `app.app_context()` when accessing Flask-specific functionality.

2. **Circular Import**:
   Avoid importing `app` in modules where `app` is already initializing.

3. **Scheduler Already Running**:
   Check for duplicate `scheduler.start()` calls and use `scheduler.running` to verify the scheduler state.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request with a detailed explanation of your changes.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or support, please contact **Mohamed Yassine Zorgui** at [zorguimohamedyassine@gmail.com].
