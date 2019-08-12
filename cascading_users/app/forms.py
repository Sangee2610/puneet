from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    #add_user = SubmitField('Add user')
    #remove_user = SubmitField('Remove user')
    submit = SubmitField('submit') 

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        print("\n\n\nuser",user)
        if user is not None:
            raise ValidationError('Please use a different username.')

class AddForm(FlaskForm):
    username1 = StringField('Username', validators=[DataRequired()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    username2 = StringField('Username', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired()])
    #add_user = SubmitField('Add user')
    #remove_user = SubmitField('Remove user')
    submit = SubmitField('submit') 

    def validate_username(self, username1):
        user = User.query.filter_by(username1=username1.data).first()
        print("\n\n\nuser",user)
        if user is not None:
            raise ValidationError('Please use a different username.')
    def validate_username(self, username2):
        user = User.query.filter_by(username2=username2.data).first()
        print("\n\n\nuser",user)
        if user is not None:
            raise ValidationError('Please use a different username.')
