# Generated by Django 2.1 on 2020-04-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_auto_20200422_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='body',
            field=models.IntegerField(verbose_name=(1, 2, 3, 4)),
        ),
    ]