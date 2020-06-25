from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, NumberRange

class ScreenNameForm(FlaskForm):
    screen_name = StringField('Screen name',[DataRequired()])
    num_tweets  = IntegerField('Number Of Tweets',validators=[DataRequired(), NumberRange(min=1,max=20)])
    model       = SelectField('Classify model by',choices=[('Tweets','Tweets'), ('Account', 'Account')])
    submit      = SubmitField('Submit')

class UserIdForm(FlaskForm):
    user_id     = StringField('User ID',[DataRequired()])
    num_tweets  = IntegerField('Number Of Tweets', validators=[DataRequired(), NumberRange(min=1,max=20)])
    model       = SelectField('Classify model by', choices=[('Tweets', 'Tweets'), ('Account', 'Account')])
    submit      = SubmitField('Submit')