# Generated by Django 2.2.7 on 2020-02-10 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20200210_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activityitem',
            old_name='position',
            new_name='activity',
        ),
    ]