from django.urls import path

from .views import (
    listaJuzgados,
    homeJuzgado
    )

urlpatterns = [
    path('juzgado/',homeJuzgado.as_view(), name='juzgado' ),
    path('juzgados/lista/',listaJuzgados.as_view(), name='lista_juzgados' ),
    
]