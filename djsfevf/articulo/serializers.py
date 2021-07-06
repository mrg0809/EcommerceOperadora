from os import read
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Categoria, Articulo, SubFamilia, SubCategoria, Familia, Marca, Talla, Variante



class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [
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
            "get_miniatura",            
        ]

class VarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variante
        fields = ["modelo", "upc", "cantidad"]