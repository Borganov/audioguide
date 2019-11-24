from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    img = models.ImageField()
    state = models.BooleanField()
    date = models.DateTimeField('date published')
