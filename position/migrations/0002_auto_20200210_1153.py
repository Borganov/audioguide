# Generated by Django 2.2.7 on 2020-02-10 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='positionitem',
            name='audio',
            field=models.FileField(default='static/audio/test4.mp3', upload_to='static/audio/'),
        ),
        migrations.AlterField(
            model_name='position',
            name='img',
            field=models.ImageField(default='static/img/default_image.jpg', upload_to='static/img'),
        ),
        migrations.AlterField(
            model_name='positionitem',
            name='lang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activity.Language'),
        ),
    ]
