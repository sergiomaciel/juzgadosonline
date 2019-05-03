from django.urls import path
from . import views

urlpatterns = [
    path('extractor/listar/', views.list_despachos),
    path('extractor/buscar/', views.buscar_despachos),
    path('extractor/cargar/', views.cargar),
]