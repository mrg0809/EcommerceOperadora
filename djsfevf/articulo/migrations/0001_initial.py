# Generated by Django 3.2.4 on 2021-06-25 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='SubFamilia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=5)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=18)),
                ('slug', models.SlugField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('miniatura', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True)),
                ('categoria', models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articulos', to='articulo.categoria')),
                ('familia', models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articulos', to='articulo.familia')),
                ('marca', models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articulos', to='articulo.marca')),
                ('subcategoria', models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articulos', to='articulo.subcategoria')),
                ('subfamilia', models.ForeignKey(default='SIN DEFINIR', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='articulos', to='articulo.subfamilia')),
                ('talla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to='articulo.talla')),
            ],
            options={
                'ordering': ('-fecha_agregado',),
            },
        ),
    ]
