# Generated by Django 3.2.4 on 2021-06-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0005_auto_20210629_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variante',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
