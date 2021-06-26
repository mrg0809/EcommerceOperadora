from django.db.models import fields
from rest_framework import serializers
from .models import Categoria, Articulo, Talla, SubFamilia, SubCategoria, Familia, Marca

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = (
            "id",
            "modelo",
            "talla",
            "descripcion",
            "precio",
            "upc",
            "familia",
            "subfamilia",
            "categoria",
            "subcategoria",
            "get_absolute_url",
            "get_image",
            "get_miniatura"
        )