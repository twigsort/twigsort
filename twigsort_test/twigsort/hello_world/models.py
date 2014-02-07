from django.db import models

# Create your models here.

class Poll(models.Model):
    '''
    question:
    pub_date:
    '''
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    '''
    poll:
    choice_text:
    votes:
    '''
    poll = models.ForeginKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)