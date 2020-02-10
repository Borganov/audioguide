from django.db import models

from audioguide import settings


def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + '/static/img'.format(instance.client_order.invoice, filename)


# Create your models here.
class Activity(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')
    isActive = models.BooleanField(default=True)
    prestataire = models.CharField(max_length=200, default='prestataire name')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    objects = models.Manager()
    lang = models.ForeignKey('Language', on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return '{title} - {description} - {img}'.format(title=self.title, description = self.description, img = self.img)

    def __unicode__(self):
        return self.description


class Language(models.Model):
    abreviation = models.CharField(max_length=10, verbose_name="abreviation")
    designation = models.CharField(max_length=15, verbose_name="Langue")
    img = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')
    isActive = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return '{designation}'.format(designation=self.designation)

    def __unicode__(self):
        return self.designation

