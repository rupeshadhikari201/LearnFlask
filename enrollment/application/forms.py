from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, EmailField, IntegerField,PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    cnfpassword = PasswordField(label="Confirm Password", validators=[DataRequired()])
    lastname = PasswordField(label="Firstname")
    lastname = StringField(label="Lastname")
    submit = SubmitField(label="Register")
    
    
class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")