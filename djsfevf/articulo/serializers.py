from os import read
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField
from rest_framework import serializers
from .models import Categoria, Articulo, SubFamilia, SubCategoria, Familia, Marca, VarianteArticulo



class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = [
            "id",
            "modelo",
            "marca",
            "descripcion",
            "precio",
            "preciodescuento",
            "familia",
            "subfamilia",
            "categoria",
            "subcategoria",
            "get_absolute_url",
            "get_image",
            "get_miniatura",    
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

class VarianteArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = VarianteArticulo
        fields = [
            "talla",
            "inventario",
            "upc",
        ]

class ArticuloDetalleSerializer(serializers.ModelSerializer):
    variantes = serializers.SerializerMethodField()
    class Meta:
        model = Articulo
        fields = [
            "id",
            "modelo",
            "marca",
            "descripcion",
            "precio",
            "preciodescuento",
            "familia",
            "subfamilia",
            "categoria",
            "subcategoria",
            "get_absolute_url",
            "get_image",
            "get_miniatura",
            "variantes"    
        ]

    def get_variantes(self,obj):
        return VarianteArticuloSerializer(obj.variantearticulo_set.all(), many=True).data