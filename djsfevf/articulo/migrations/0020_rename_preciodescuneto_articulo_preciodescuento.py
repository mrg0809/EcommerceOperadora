# Generated by Django 3.2.4 on 2021-08-01 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0019_articulo_preciodescuneto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='preciodescuneto',
            new_name='preciodescuento',
        ),
    ]
