from django.http import Http404
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Articulo, Familia, Marca, SubFamilia
from .serializers import ArticuloSerializer, SubFamiliaSerializer, MarcaSerializer, ArticuloDetalleSerializer

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
            print(Articulo.objects.filter(modelo = modelo_id))
            return Articulo.objects.filter(modelo = modelo_id)
        except Articulo.DoesNotExist:
            raise Http404

    def get(self, request, subfamilia_slug, articulo_slug, format=None):
        articulo = self.get_object(subfamilia_slug, articulo_slug)
        serializer = ArticuloDetalleSerializer(articulo)
        return Response(serializer.data)

class SubFamiliaDetalle(APIView):
    def get_object(self, subfamilia_slug):
        try:
            return SubFamilia.objects.get(slug=subfamilia_slug)
        except Articulo.DoesNotExist:
            raise Http404

    def get(self, request, subfamilia_slug, format=None):
        subfamilia = self.get_object(subfamilia_slug)
        serializer = SubFamiliaSerializer(subfamilia)
        return Response(serializer.data)

class MarcaDetalle(APIView):
    def get_object(self, marca_slug):
        try:
            return Marca.objects.get(slug=marca_slug)
        except Articulo.DoesNotExist:
            raise Http404

    def get(self, request, marca_slug, format=None):
        marca = self.get_object(marca_slug)
        serializer = MarcaSerializer(marca)
        return Response(serializer.data)

@api_view(['POST'])
def buscar(request):
    busqueda = request.data.get('busqueda', '')
    if busqueda:
        articulos = Articulo.objects.filter(Q(modelo__icontains=busqueda) | Q(descripcion__icontains=busqueda))
        serializer = ArticuloSerializer(articulos, many=True)
        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({"articulos": []})