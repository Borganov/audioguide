# Generated by Django 2.2.7 on 2020-02-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_auto_20191201_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='activity',
            name='lang',
            field=models.CharField(max_length=2, verbose_name='Langue'),
        ),
    ]
