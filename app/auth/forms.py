from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField,PasswordField,ValidationError
from wtforms.validators import Required, EqualTo, Email
from flask_wtf.file import FileField, FileRequired
from ..models import User,Comment,Post

class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name", validators = [Required()])
    username = StringField("Userame", validators = [Required()])
    email = StringField("Email",validators = [Required(),Email()])
    password = PasswordField("Password", validators = [Required(),EqualTo("pass_confirm", message = "Passwords do not match")])
    pass_confirm = PasswordField("Confirm Password", validators = [Required()])
    submit = SubmitField("Register")