from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ScreenNameForm(FlaskForm):
    screen_name = StringField('Screen name',[
        DataRequired()
    ])
    submit = SubmitField('Submit')

class UserIdForm(FlaskForm):
    user_id = StringField('User ID',[
        DataRequired()
    ])
    submit = SubmitField('Submit')