from django.urls import path

from .views import (
    vistaExpediente,
    Subscriptores,
    vistaListaExpedientes,
    vistaApp
    )

urlpatterns = [
    path('app',vistaApp.as_view(), name='app' ),
    path('expedientes',vistaListaExpedientes.as_view(), name='lista_expedientes' ),
    path('expediente/<int:pk>/',vistaExpediente.as_view(), name='expediente' ),
     path('expediente/<int:pk>/',Subscriptores.as_view(), name='suscripcion' ),
]