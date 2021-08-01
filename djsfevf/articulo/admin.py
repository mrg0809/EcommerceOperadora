from django.contrib import admin
from .models import Articulo, Marca, Familia, SubFamilia, Categoria, SubCategoria, VarianteArticulo
# Register your models here.


class VarianteArticuloAdmin(admin.ModelAdmin):
    list_display = [
        'talla',
        'inventario',
        'upc',
        'padre',
    ]
    list_filter = ['talla', 'padre']

class VarianteArticuloInLineAdmin(admin.TabularInline):
    model = VarianteArticulo
    extra = 1


class ArticuloAdmin(admin.ModelAdmin):
    list_display = [
        'modelo', 
        'marca', 
        'familia', 
        'subfamilia', 
        'categoria', 
        'subcategoria', 
        'descripcion',
        'precio',
        'preciodescuento'
        ]
    inlines = [VarianteArticuloInLineAdmin]

admin.site.register(VarianteArticulo, VarianteArticuloAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Marca)
admin.site.register(Familia)
admin.site.register(SubFamilia)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
