# Generated by Django 3.2.4 on 2021-07-06 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0008_alter_variante_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variante',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulo.articulo'),
        ),
    ]
