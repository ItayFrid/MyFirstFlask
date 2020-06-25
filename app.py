from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect

from Engine.Predictor import Predictor
from config import Config
from tweepy import OAuthHandler, API
from form import ScreenNameForm, UserIdForm
from random import sample

app = Flask(__name__)
app.config.from_object(Config)
Bootstrap(app)

def get_tweets(screen_name=None,user_id=None,numberOfTweets=20,model='Tweets'):
    predictor = Predictor()
    # Connect to Twitter API
    auth = OAuthHandler(app.config['CONSUMER_KEY'],
                        app.config['CONSUMER_SECRET'])
    auth.set_access_token(app.config['ACCESS_TOKEN'],
                          app.config['ACCESS_TOKEN_SECRET'])
    api = API(auth)
    try:
        if screen_name is not None:
            timeline    = api.user_timeline(screen_name = screen_name)
            user        = api.get_user(screen_name = screen_name)
        else:
            timeline    = api.user_timeline(user_id = user_id)
            user        = api.get_user(user_id = user_id)
        tweets = []
        numTweets = sample(range(20), numberOfTweets)
        counter = 0
        #Getting the tweets ready for proccess
        for tweet in timeline:
            if counter in numTweets:
                twt = {}
                twt['created_at']       = tweet.created_at
                twt['id']               = tweet.id
                twt['text']             = tweet.text
                twt['retweet_count']    = tweet.retweet_count
                twt['retweeted']        = tweet.retweeted
                twt['favorite_count']   = tweet.favorite_count
                twt['hashtags']         = process_hashtags(tweet.entities['hashtags'])
                twt['mentions']         = process_mentions(tweet.entities['user_mentions'])
                twt['lang']             = tweet.lang
                tweets.append(twt)
            counter+=1
        #Getting user details ready for proccess
        userDetails = {}
        userDetails['name']             = user.name
        userDetails['created_at']       = user.created_at
        userDetails['location']         = user.location
        userDetails['followers_count']  = user.followers_count
        userDetails['statuses_count']   = user.statuses_count
        userDetails['screen_name']      = user.screen_name
        userDetails['favourites_count'] = user.favourites_count
        userDetails['friends_count']    = user.friends_count
        userDetails['listed_count']     = user.listed_count
        userDetails['description']      = user.description
        userDetails['profile_pic']      = user.profile_image_url_https
        # predicting
        predictor.setInput([userDetails],tweets)
        predictor.process()
        predictions, threshold, classes, final = predictor.predict()
        return predictions, threshold, classes, final, userDetails, tweets
    except Exception as e:
        print('error', e)
        return None

# Utility function
def process_hashtags(hashtags):
    lst = []
    for h in hashtags:
        lst.append(h['text'])
    return lst

# Utility function
def process_mentions(mentions):
    lst=[]
    for m in mentions:
        lst.append(m['screen_name'])
        return lst

@app.route('/', methods=('GET', 'POST'))
def index():
    screenForm = ScreenNameForm()
    userIdForm = UserIdForm()
    if screenForm.validate_on_submit():
        return redirect(url_for('screen_name',
                                screen_name = screenForm.screen_name.data,
                                num_tweets = screenForm.num_tweets.data,
                                model = screenForm.model.data))
    if userIdForm.validate_on_submit():
        return redirect(url_for('user_id',
                                user_id=userIdForm.user_id.data,
                                num_tweets = userIdForm.num_tweets.data,
                                model = userIdForm.model.data))
    return render_template('index.html',screenForm = screenForm,userIdForm = userIdForm)

@app.route('/<model>/screen_name/<screen_name>/<num_tweets>')
def screen_name(model,screen_name,num_tweets):
    if num_tweets is not None:
        num = int(num_tweets)
    else:
        num = 20
    predictions, threshold, classes, final, userDetails, tweets = get_tweets(screen_name=screen_name,numberOfTweets=num,model=model)
    if userDetails is None or len(userDetails) == 0:
        return redirect(url_for('error',message = 'User or tweets does not exists'))
    return render_template('screenNameTweets.html',**locals())

@app.route('/<model>/user_id/<user_id>/<num_tweets>')
def user_id(model,user_id=None,num_tweets=None):
    if num_tweets is not None:
        num = int(num_tweets)
    else:
        num = 20
    predictions, threshold, classes, final, userDetails, tweets = get_tweets(user_id=user_id,numberOfTweets=num,model=model)
    if userDetails is None or len(userDetails) == 0:
        return redirect(url_for('error',message = 'User or tweets does not exists'))
    return render_template('userIdTweets.html',**locals())

@app.route('/error/<message>')
def error(message):
    return render_template('error.html',**locals())

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')