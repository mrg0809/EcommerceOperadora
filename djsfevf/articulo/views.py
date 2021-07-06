from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Articulo, Variante
from .serializers import ArticuloSerializer, VarianteSerializer

class NuevosProductos(APIView):
    def get(self,request, format=None):
        articulos = Articulo.objects.all()[0:4]
        serializer = ArticuloSerializer(articulos, many=True)
        return Response(serializer.data)

class DetalleProducto(APIView):
    def get_object(self, subfamilia_slug, articulo_slug):
        try:
            return Articulo.objects.filter(subfamilia__slug=subfamilia_slug).get(slug=articulo_slug)
        except Articulo.DoesNotExist:
            raise Http404
        
    def get_variante(self, modelo_id):
        try:
            print(Variante.objects.filter(modelo = modelo_id))
            return Variante.objects.filter(modelo = modelo_id)
        except Variante.DoesNotExist:
            raise Http404

    def get(self, request, subfamilia_slug, articulo_slug, format=None):
        articulo = self.get_object(subfamilia_slug, articulo_slug)
        serializer = ArticuloSerializer(articulo)
        variante = self.get_variante(serializer.data.get('id'))
        serializer2 = VarianteSerializer(variante)
        print(serializer2.data)
        return Response(serializer.data)