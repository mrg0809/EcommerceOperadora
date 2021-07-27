from django.contrib import admin
from .models import Articulo, Marca, Familia, SubFamilia, Categoria, SubCategoria, Talla, Tallaje, Variante
# Register your models here.

class VariantesInline(admin.TabularInline):
    model = Variante
    extra = 1
    show_change_link = True

class TallaInline(admin.TabularInline):
    model = Talla
    extra = 1
    show_change_link = True

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
        ]
    inlines = [VariantesInline]

class TallajeAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
    ]
    inlines = [TallaInline]


admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Marca)
admin.site.register(Familia)
admin.site.register(SubFamilia)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Talla)
admin.site.register(Variante)
admin.site.register(Tallaje, TallajeAdmin)