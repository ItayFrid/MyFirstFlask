import os

class Config(object):
    SECRET_KEY          = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    CONSUMER_KEY        = 'XkzkavT1AYCbdKl4YtL5uzYyd'
    CONSUMER_SECRET     = 'mxH3coDZh9iK5IQfOqCcBHlBXJqQPESyimOzqnzTK8uhsXDXd1'
    ACCESS_TOKEN        = '1318107410-W35PhlRbyRkrAcoBqzKi5a8yLPe1WjrF7wqPdz7'
    ACCESS_TOKEN_SECRET = 'hLWdwiFo2R4iL2xjdIZuQYwEjmbvjZvOEGJ5EJzDF5v2h'