from django.db import models
from articulo.models import Articulo

# Create your models here.
class Orden(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    adress2 = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=7)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    created_at = models.DateField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.first_name


class ArticuloOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='articulos', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, related_name='articulos', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id
            

