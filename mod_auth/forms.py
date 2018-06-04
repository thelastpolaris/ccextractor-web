"""
ccextractor-web | mod_auth/forms.py

Author   : Saurabh Shrivastava
Email    : saurabh.shrivastava54@gmail.com
Link     : https://github.com/saurabhshr

Based on https://github.com/CCExtractor/sample-platform/blob/master/mod_auth/forms.py
Author   : Willem Van Iseghem
Email    : github@canihavesome.coffee
Link     : https://github.com/canihavesomecoffee
"""

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, ValidationError

def valid_password(form, field):
    pass_size = len(field.data)
    if pass_size == 0:
        raise ValidationError('The password can not be empty!')
    if pass_size < 8 or pass_size > 50:
        raise ValidationError(
            'Password needs to be between 8 and 50 characters long (you entered {char})'.format(char=pass_size)
        )

class SignupForm(FlaskForm):
    name = StringField('Name', [DataRequired(message='Name is not filled in.')])
    email = EmailField('Email', [DataRequired(message='Email address is not filled in'),
                                 Email(message='Entered value is not a valid email address')])
    password = PasswordField('Password', [DataRequired(message='Password is not filled in.'), valid_password])
    password_repeat = PasswordField('Repeat password', [DataRequired(message='Repeated password is not filled in.')])
    submit = SubmitField('Register')

    @staticmethod
    def validate_password_repeat(form, field):
        if field.data != form.password.data:
            raise ValidationError('The password needs to match the new password')

class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(message='Email address is not filled in'),
                                 Email(message='Entered value is not a valid email address')])
    password = PasswordField('Password', [DataRequired(message='Password cannot be empty.')])
    submit = SubmitField('Login')


