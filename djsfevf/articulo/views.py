from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Articulo
from .serializers import ArticuloSerializer

class NuevosProductos(APIView):
    def get(self,request, format=None):
        articulos = Articulo.objects.all()[0:4]
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

# Create your views here.
