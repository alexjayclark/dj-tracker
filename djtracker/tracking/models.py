from django.db import models

class Article(models.Model):
    headline = models.TextField()
    pub_date = models.DateField()
    text = models.TextField()
    tweet_text = models.TextField()
    tweet_date = models.DateTimeField()
    has_data = models.BooleanField()
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
        super(Model, self).save(*args, **kwargs)
