# Generated by Django 2.1 on 2020-04-29 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='body',
            field=models.IntegerField(verbose_name=(0, 1, 2, 3, 4)),
        ),
    ]
