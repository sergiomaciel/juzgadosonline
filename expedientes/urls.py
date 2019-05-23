from django.urls import path

from .views import (
    vistaExpediente,
    vistaListaExpedientes,
    vistaApp
    )

urlpatterns = [
    path('app',vistaApp.as_view(), name='app' ),
    path('app/expedientes',vistaListaExpedientes.as_view(), name='lista_expedientes' ),
    path('app/expediente/<int:pk>/',vistaExpediente.as_view(), name='expediente' ),
]