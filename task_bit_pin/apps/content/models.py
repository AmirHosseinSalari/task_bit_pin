from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return f'{self.title} | {self.id}'


class Score(models.Model):
    content_id = models.ForeignKey(
        Content, related_name='scores', on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User, related_name='scores_users', on_delete=models.CASCADE)
    stars = models.IntegerField()

    def __str__(self):
        return '%d: %s' % (self.score, self.user_id)
