"""
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djtracker.settings")
import twitter
from newspaper import Article
from tracker.models import Paper, Story

def scrape_tweets():
    api = twitter.Api(consumer_key='s3mqSn9ziQ7dTtvDXsZKn7u5W',
                 consumer_secret='lSfOUJU5XnWzoO52xsMUSSE0zOo7iCGHWaRjmLObMuklg1aqXP',
                 access_token_key='983993198166102016-PDn5RC9SeppJ1Ci3yy36xWAVYVl2SYy',
                 access_token_secret='b5Wo5CChlv4bOZ2D37CU8Z2CmG8arGX92ggJa0W6Tafgp',
                 tweet_mode='extended',
                 sleep_on_rate_limit=True)
    papers = Paper.objects.all()
    for paper in
"""
