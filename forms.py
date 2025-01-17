from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class TaskForm(FlaskForm):
    volet = StringField('Volet', validators=[DataRequired()])
    action_programmee = StringField('Action programmée', validators=[DataRequired()])
    periodicite = StringField('Périodicité', validators=[DataRequired()])
    responsable = StringField('Responsable', validators=[DataRequired()])
    echeance_prochaine = DateField('Echéance Prochaine', validators=[DataRequired()])
    acteurs_externes = StringField('Acteurs externes')
    submit = SubmitField('Add Task')
