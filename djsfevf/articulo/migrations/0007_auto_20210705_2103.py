# Generated by Django 3.2.4 on 2021-07-06 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0006_alter_variante_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_categoria', to='articulo.categoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='familia',
            field=models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_familia', to='articulo.familia'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='marca',
            field=models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_marca', to='articulo.marca'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='subcategoria',
            field=models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_subcategoria', to='articulo.subcategoria'),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='subfamilia',
            field=models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='related_subfamilia', to='articulo.subfamilia'),
        ),
        migrations.AlterField(
            model_name='variante',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_modelo', to='articulo.articulo'),
        ),
        migrations.AlterField(
            model_name='variante',
            name='talla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_talla', to='articulo.talla'),
        ),
    ]
