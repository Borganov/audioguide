# Generated by Django 2.2.7 on 2020-02-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0004_auto_20200211_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='order',
            field=models.FloatField(),
        ),
    ]
