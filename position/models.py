from django.db import models

from audioguide import settings


def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/imgPosition'.format(instance.client_order.invoice, filename)


# Create your models here.
class Position(models.Model):
    lang = models.CharField(max_length=2, verbose_name="Langue")
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    objects = models.Manager()
    state = models.BooleanField()

    def __str__(self):
        return '{order} - {name}'.format(order = self.order, name = self.name)

    def __unicode__(self):
        return self.name

class PositionItem(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    order = models.IntegerField()
    lang = models.CharField(max_length=2, verbose_name="Langue")
    audio = models.FileField(upload_to='static/audio/', default='static/audio/test4.mp3')
    img = models.ImageField(upload_to='static/imgPosition')
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    objects = models.Manager()
    state = models.BooleanField()

    def __str__(self):
        return '{position} - {titre} - {description}'.format(position = self.position, titre = self.titre, description = self.description)

    def __unicode__(self):
        return self.position.name



