from django.db import models

from audioguide import settings
from activity.models import Language

def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/img'.format(instance.client_order.invoice, filename)


# Create your models here.
class Position(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    objects = models.Manager()
    isActive = models.BooleanField(default=True)
    img = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')

    def __str__(self):
        return '{order} - {name}'.format(order = self.order, name = self.name)

    def __unicode__(self):
        return self.name

class PositionItem(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    lang = models.ForeignKey('activity.Language', on_delete=models.DO_NOTHING)
    audio = models.FileField(upload_to='static/audio/', default='static/audio/test4.mp3')
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return '{positionOrder} - {positionImg} - {audioUrl} - {titre} - {description}'.format(positionOrder = self.position.order, positionImg = self.position.img, audioUrl = self.audio, titre = self.titre, description = self.description)

    def __unicode__(self):
        return self.position.name
