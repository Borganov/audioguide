from django.db import models

def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/imgPosition'.format(instance.client_order.invoice, filename)

# Create your models here.
class Position(models.Model):
    order = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/imgPosition')


class PositionItem(models.Model):
    titre = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    lang = models.CharField(max_length=2)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
