from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField, PasswordField
)




class LoginForm(FlaskForm):
    employee_number = StringField("Employee number", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")