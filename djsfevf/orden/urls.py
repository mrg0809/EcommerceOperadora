from django.urls import path
from django.urls.resolvers import URLPattern
from orden import views

urlpatterns = [
    path('checkout/', views.checkout)
]