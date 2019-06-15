from django.urls import path

from .views import (
    vistaExpediente,
    vistaApp,
    vistaMisExpedientes,
    crearExpediente,
    actualizarExpediente,
    borrarExpediente,
    buscarExpediente
    )

urlpatterns = [
    path('app/',vistaApp.as_view(), name='dashboard' ),
    path('app/mis-expedientes/',vistaMisExpedientes.as_view(), name='mis_expedientes' ),
    path('app/expediente/nuevo/',crearExpediente.as_view(), name='nuevo_expediente' ),
    path('app/expediente/actualizar/<int:pk>/',actualizarExpediente.as_view(), name='actualizar_expediente' ),
    path('app/expediente/borrar/<int:pk>/',borrarExpediente.as_view(), name='borrar_expediente' ),
    path('app/expediente/buscar/',buscarExpediente.as_view(), name='buscar' ),
    path('app/expediente/<int:pk>/',vistaExpediente.as_view(), name='expediente' ),
]