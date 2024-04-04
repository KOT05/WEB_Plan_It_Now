from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.simple import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired()])
    # remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Register')


#TODO закончить файл с регистрацией