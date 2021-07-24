from os import read
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Categoria, Articulo, SubFamilia, SubCategoria, Familia, Marca, Talla, Variante


class VarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variante
        fields = [
            "modelo", 
            "upc",
            "cantidad",
            ]


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        related_articulo = VarianteSerializer(many=True)
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
            "related_articulo",           
        ]

class SubFamiliaSerializer(serializers.ModelSerializer):
    subfamilia = ArticuloSerializer(many=True) 
    class Meta:
        model = SubFamilia
        fields = [
            "id",
            "nombre",
            "get_absolute_url",
            "subfamilia",
        ]

class MarcaSerializer(serializers.ModelSerializer):
    marca = ArticuloSerializer(many=True) 
    class Meta:
        model = Marca
        fields = [
            "id",
            "nombre",
            "get_absolute_url",
            "marca",
        ]