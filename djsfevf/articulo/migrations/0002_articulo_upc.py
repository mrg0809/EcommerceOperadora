# Generated by Django 3.2.4 on 2021-06-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='upc',
            field=models.CharField(default=8888888888, max_length=18),
            preserve_default=False,
        ),
    ]
