# Generated by Django 3.2.4 on 2021-07-26 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0014_auto_20210726_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='variantes',
        ),
    ]
