from datetime import datetime
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(minutes=5)
        # this check if the pub_date is 5 minutes older or note timedelta(day or minute) gives time excalty that day or minutes earlier than now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default= 0)
    def __str__(self):
        return self.choice_text