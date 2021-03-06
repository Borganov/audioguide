from django.db import models

from audioguide import settings


def image_upload_path(instance, filename):
    return settings.MEDIA_ROOT + 'static/img'.format(instance.client_order.invoice, filename)


# Create your models here.
class Activity(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')
    isActive = models.BooleanField(default=True)
    prestataire = models.CharField(max_length=200, default='prestataire name')
    date = models.DateTimeField(auto_now_add=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return '{number} - {title} - {prestataire}'.format(number= self.number, title=self.title, prestataire=self.prestataire)

    def __unicode__(self):
        return self.title

class ActivityItem(models.Model):
    lang = models.ForeignKey('activity.Language', on_delete=models.DO_NOTHING, default=1)
    order = models.FloatField(default=1)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    objects = models.Manager()
    isActive = models.BooleanField(default=True)
    activity = models.ForeignKey('Activity', on_delete=models.CASCADE)

    def __str__(self):
        return '{activityNumber} -  {description} - {activityImg} - {order} - {prestataire}'.format(activityNumber = self.activity.number,  description = self.description, activityImg = self.activity.img, order = self.order, prestataire=self.activity.prestataire)

    def __unicode__(self):
        return self.activity.title


class Language(models.Model):
    abreviation = models.CharField(max_length=10, verbose_name="abreviation", default="fr")
    designation = models.CharField(max_length=15, verbose_name="Langue")
    img = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')
    imgMouse = models.ImageField(upload_to='static/img', default='static/img/default_image.jpg')
    isActive = models.BooleanField(default=True)
    objects = models.Manager()

    def __str__(self):
        return '{designation}'.format(designation=self.designation)

    def __unicode__(self):
        return self.designation
