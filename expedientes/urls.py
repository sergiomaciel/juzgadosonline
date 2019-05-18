from django.urls import path

from .views import vistaExpediente, vistaListaExpedientes, vistaApp

urlpatterns = [
    path('app',vistaApp.as_view(), name='app' ),
    path('expedientes',vistaListaExpedientes.as_view(), name='lista_expedientes' ),
    path('expediente/<int:pk>/',vistaExpediente.as_view(), name='expediente' ),
]