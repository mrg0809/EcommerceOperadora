from django.db.models import fields
from rest_framework import serializers
from .models import Orden, ArticuloOrden
from articulo.serializers import ArticuloSerializer

class ArticuloOrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticuloOrden
        fields = (
            "articulo",
            "cantidad",
            "precio",
        )

class OrdenSerializer(serializers.ModelSerializer):
    articulos = ArticuloOrdenSerializer(many=True)
    class Meta:
        model = Orden
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "adress",
            "adress2",
            "zipcode",
            "city",
            "phone",
            "stripe_token",
            "articulos",
        )

    def create(self, validated_data):
        articulos_data = validated_data.pop('articulos')
        orden = Orden.objects.create(**validated_data)

        for articulo_data in articulos_data:
            ArticuloOrden.objects.create(orden=orden, **articulo_data)

        return orden