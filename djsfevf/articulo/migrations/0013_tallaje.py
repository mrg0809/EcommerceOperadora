# Generated by Django 3.2.4 on 2021-07-26 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0012_alter_articulo_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tallaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talla', to='articulo.talla')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
    ]