from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import InputRequired, Email, EqualTo

class SignUpForm(FlaskForm):
    full_name = StringField('Full Name')
    email = StringField('Email',
                        validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators = [InputRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators = [InputRequired()])
    submit = SubmitField('Login')

class PetForm(FlaskForm):
    name = StringField('Pet"s Name', validators = [InputRequired()])
    age = StringField('Pet"s Age', validators = [InputRequired()])
    bio = StringField('Pet"s Bio', validators = [InputRequired()])
    submit = SubmitField('Edit Pet')

class InsertPetForm(FlaskForm):
    name = StringField('Pet"s Name', validators = [InputRequired()])
    age = StringField('Pet"s Age', validators = [InputRequired()])
    bio = StringField('Pet"s Bio', validators = [InputRequired()])
    image = FileField('Upload an image')
    submit = SubmitField('Insert Pet')