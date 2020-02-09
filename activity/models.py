from django.db import models

from audioguide import settings


def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/imgActivity'.format(instance.client_order.invoice, filename)


# Create your models here.
class Activity(models.Model):
    lang = models.CharField(max_length=2, verbose_name="Langue")
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='static/imgActivity')
    state = models.BooleanField()
    site = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{title} - {description} - {img}'.format(title=self.title, description = self.description, img = self.img)

    def __unicode__(self):
        return self.name
