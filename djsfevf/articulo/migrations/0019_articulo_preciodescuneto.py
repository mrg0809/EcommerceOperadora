# Generated by Django 3.2.4 on 2021-08-01 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0018_variantearticulo_inventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='preciodescuneto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]