from django.contrib import admin
from .models import Articulo, Marca, Familia, SubFamilia, Categoria, SubCategoria, Talla
# Register your models here.

admin.site.register(Articulo)
admin.site.register(Marca)
admin.site.register(Familia)
admin.site.register(SubFamilia)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Talla)
