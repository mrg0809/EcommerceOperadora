import stripe

from django.conf import settings
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Orden, ArticuloOrden
from .serializers import OrdenSerializer

@api_view(['POST'])
def checkout(request):
    serializer = OrdenSerializer(data=request.data)

    print(OrdenSerializer.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(articulo.get('cantidad') * articulo.get('articulo').precio for articulo in serializer.validated_data['articulos'])

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='MXN',
                description='EVFstore Sportsfan',
                source=serializer.validated_data['stripe_token']
            )

            serializer.save(paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)