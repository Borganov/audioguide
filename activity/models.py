from django.db import models

from audioguide import settings


def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/imgActivity'.format(instance.client_order.invoice, filename)


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='static/imgActivity')
    state = models.BooleanField()
    date = models.DateTimeField('date published')
    lang = models.CharField(max_length=2, verbose_name="Langue")
