# Generated by Django 2.2.6 on 2019-12-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_activity_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='img',
            field=models.ImageField(upload_to='static/imgActivity'),
        ),
    ]