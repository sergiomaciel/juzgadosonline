from django.urls import path

from .views import ListarDespachos
from .views.funciones import buscar_despachos,cargar

urlpatterns = [
    path('extractor/despachos/',ListarDespachos.as_view(), name='listar_despacho' ),
    path('extractor/buscar/', buscar_despachos),
    path('extractor/cargar/', cargar),
]