# Generated by Django 2.2.7 on 2020-02-10 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0007_auto_20200210_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='activityitem',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
