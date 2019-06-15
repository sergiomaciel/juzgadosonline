from django.urls import path

from .views import (
    listaJuzgados
    )

urlpatterns = [
    path('app/juzgados/',listaJuzgados.as_view(), name='juzgados' ),
]