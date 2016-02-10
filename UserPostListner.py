from twitter import *
import os

OAUTH = os.path.expanduser('~/.twitter_oauth')
CONSUMER_KEYS = os.path.expanduser('~/.twitter_cons')
USERNAME = '@c0nt41n3d'

oauth_token, oauth_secret = read_token_file(OAUTH)
con_key, con_secret = read_token_file(CONSUMER_KEYS)
auth = OAuth(consumer_key=con_key, consumer_secret=con_secret, token=oauth_token, token_secret=oauth_secret)
stream = TwitterStream(auth=auth, domain='userstream.twitter.com')

for tweet in stream.user():
    text = tweet.get('text')
    if text is not None:
        if USERNAME in text:
            text = text[len(USERNAME) + 1:]
        user = tweet.get('user').get('name')
        say = user + " said " + text
        print(say)
        os.system("say " + say)
