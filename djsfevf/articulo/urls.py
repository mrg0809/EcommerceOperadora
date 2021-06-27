from django.urls import path, include
from django.urls.resolvers import URLPattern
from articulo import views

urlpatterns = [
    path('lastest-products/', views.NuevosProductos.as_view()),
    path('articulos/<slug:subfamilia_slug>/<slug:articulo_slug>/', views.DetalleProducto.as_view()),
]