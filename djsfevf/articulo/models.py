from os import MFD_ALLOW_SEALING, name
from django.core.files import File
from django.db import models
from io import BytesIO
from PIL import Image
from django.db.models.expressions import F
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey, ManyToManyField


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Marca(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'

class SubFamilia(models.Model):
    nombre = models.CharField(max_length=30)
    slug = models.SlugField()

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Articulo(models.Model):
    modelo = models.CharField(max_length=18)
    marca = models.ForeignKey(Marca, related_name='marca', on_delete=models.SET_DEFAULT, default='SIN DEFINIR')
    familia = models.ForeignKey(Familia, related_name='related_familia', on_delete=models.SET_DEFAULT, default='SIN DEFINIR')
    subfamilia = models.ForeignKey(SubFamilia, related_name='subfamilia', on_delete=models.SET_DEFAULT, default='SIN DEFINIR')
    categoria = models.ForeignKey(Categoria, related_name='related_categoria', on_delete=models.SET_DEFAULT, default='SIN DEFINIR')
    subcategoria = models.ForeignKey(SubCategoria, related_name='related_subcategoria', on_delete=models.SET_DEFAULT, default='SIN DEFINIR')
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    preciodescuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    slug = models.SlugField()
    imagen = models.ImageField(upload_to='uploads/', blank=True, null=True)
    miniatura = models.ImageField(upload_to='uploads/', blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-fecha_agregado',)

    def __str__(self):
        return self.modelo

    def get_absolute_url(self):
        return f'/{self.subfamilia.slug}/{self.slug}/'

    def get_image(self):
        if self.imagen:
            return 'http://127.0.0.1:8000' + self.imagen.url
        return ''

    def get_miniatura(self):
        if self.miniatura:
            return 'http://127.0.0.1:8000' + self.miniatura.url
        else:
            if self.imagen:
                self.miniatura = self.make_miniatura(self.imagen)
                self.save()
                return 'http://127.0.0.1:8000' + self.miniatura.url
            else:
                return ''

    def make_miniatura(self, imagen, size=(250, 250)):
        img = Image.open(imagen)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=90)
        miniatura = File(thumb_io, name=imagen.name)
        return miniatura



class VarianteArticulo(models.Model):
    padre = ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
    talla = models.CharField(max_length=5)  #S, M, L ,21, 22
    inventario = models.IntegerField(default=0)
    upc = models.CharField(max_length=15, unique=True)

    class Meta:
        unique_together = (
            ('padre', 'talla')
        )

    def __str__(self):
        return self.talla
    

    
    