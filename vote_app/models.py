from django.db import models

class PersonalAnswer(models.Model):
    direction = models.TextField()
    count = models.IntegerField()
    score = models.IntegerField()