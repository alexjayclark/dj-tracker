from django.db import models
import twitter
from newspaper import Article
import dateutil
import datetime
import time

class Paper(models.Model):
    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    def get_stories(self):
        # most_recent = self.story_set.latest('date')
        api = twitter.Api(consumer_key='s3mqSn9ziQ7dTtvDXsZKn7u5W',
                 consumer_secret='lSfOUJU5XnWzoO52xsMUSSE0zOo7iCGHWaRjmLObMuklg1aqXP',
                 access_token_key='983993198166102016-PDn5RC9SeppJ1Ci3yy36xWAVYVl2SYy',
                 access_token_secret='b5Wo5CChlv4bOZ2D37CU8Z2CmG8arGX92ggJa0W6Tafgp',
                 tweet_mode='extended',
                 sleep_on_rate_limit=True)
        tweets = [t.AsDict() for t in api.GetUserTimeline(screen_name=self.handle, count=200)]
        if len(tweets) == 0:
            pass
        else:
            still_tweets = True
            while still_tweets:
                for t in tweets:
                    if len(t['urls']) != 1:
                        continue
                    if str(t['id']) in [s.tweet_id for s in Story.objects.all()]:
                        continue
                    s = Story()
                    s.tweet_id = t['id']
                    s.tweet_text = t['full_text']
                    s.date = dateutil.parser.parse(t['created_at'])
                    s.url = t['urls'][0]['expanded_url']
                    try:
                        article = Article(s.url)
                        article.download()
                        article.parse()
                    except:
                        try:
                            time.sleep(5)
                            article = Article(s.url)
                            article.download()
                            article.parse()
                        except:
                            continue
                    s.headline = article.title
                    s.text = " ".join(article.text.split()[:200])
                    s.paper = self
                    s.save()
                last_tweet = tweets[-1]['id']
                tweets = [t.AsDict() for t in api.GetUserTimeline(screen_name=self.handle, count=200, max_id=last_tweet)][1:]
                if len(tweets) < 10:
                    still_tweets = False
                elif dateutil.parser.parse(tweets[0]['created_at']).date() < (datetime.datetime.now().date() - datetime.timedelta(days=8)):
                    still_tweets = False



class Story(models.Model):
    headline = models.TextField()
    date = models.DateTimeField()
    text = models.TextField()
    tweet_id = models.CharField(max_length=200, unique=True)
    tweet_text = models.TextField()
    url = models.CharField(max_length=200)
    has_data = models.BooleanField()
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    def __str__(self):
        return self.headline
    def search_data(self):
        to_search = self.headline + self.text + self.tweet_text
        if 'data' in to_search:
            return True
        else:
            return False
    def save(self, *args, **kwargs):
        self.has_data = self.search_data()
        super(Story, self).save(*args, **kwargs)
