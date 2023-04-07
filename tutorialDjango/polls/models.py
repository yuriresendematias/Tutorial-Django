from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    text = models.CharField("Texto", max_length=200)
    date = models.DateTimeField("data de publicação")

    def __str__(self):
        return self.text
    
    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("Texto", max_length=200)
    votes = models.IntegerField("número de votos", default=0)

    def __str__(self):
        return self.choice_text