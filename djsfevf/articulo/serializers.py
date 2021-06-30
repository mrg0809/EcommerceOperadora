from django.db.models import fields
from rest_framework import serializers
from .models import Categoria, Articulo, SubFamilia, SubCategoria, Familia, Marca, Talla, Variante

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = (
            "id",
            "modelo",
            "marca",
            "descripcion",
            "precio",
            "familia",
            "subfamilia",
            "categoria",
            "subcategoria",
            "get_absolute_url",
            "get_image",
            "get_miniatura"
        )