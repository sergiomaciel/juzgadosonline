from django.urls import path

from .views import (
    listaJuzgados,
    homeJuzgado,
    crearExpediente,
    actualizarExpediente
    )

urlpatterns = [
    path('juzgado/',homeJuzgado.as_view(), name='juzgado' ),
    path('juzgados/lista/',listaJuzgados.as_view(), name='lista_juzgados' ),
    path('juzgados/expediente/nuevo/',crearExpediente.as_view(), name='nuevo_expediente' ),
    path('juzgados/expediente/actualizar/<int:pk>/',actualizarExpediente.as_view(), name='actualizar_expediente' ),
    
]