from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class ScreenNameForm(FlaskForm):
    screen_name = StringField('Screen name',[DataRequired()])
    num_tweets  = IntegerField('Number Of Tweets',validators=[DataRequired(), NumberRange(min=1,max=20)])
    submit      = SubmitField('Submit')

class UserIdForm(FlaskForm):
    user_id     = StringField('User ID',[DataRequired()])
    num_tweets  = IntegerField('Number Of Tweets', validators=[DataRequired(), NumberRange(min=1,max=20)])
    submit      = SubmitField('Submit')