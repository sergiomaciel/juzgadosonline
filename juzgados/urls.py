from django.urls import path

from .views import (
    listaJuzgados,
    homeJuzgado,
    crearExpediente,
    actualizarExpediente,
    crearActualizacion,
    actualizarActualizacion,
    borrarActualizacion,
    loginView
    )

urlpatterns = [
    path('juzgado/',homeJuzgado.as_view(), name='juzgado' ),
    path('juzgado/lista/',listaJuzgados.as_view(), name='lista_juzgados' ),
    # Expediente
    path('juzgado/expediente/nuevo/',crearExpediente.as_view(), name='nuevo_expediente' ),
    path('juzgado/expediente/<int:pk>/',actualizarExpediente.as_view(), name='CRUD_expediente' ),
    # Actualizacion
    path('juzgado/nueva-actualizacion/<int:pk>/',crearActualizacion.as_view(), name='nueva_actualizacion' ),
    path('juzgado/actualizacion/<int:id_Act>/<int:id_Exp>/',actualizarActualizacion.as_view(), name='actualizacion' ),
    path('juzgado/actualizacion/borrar/<int:pk>/',borrarActualizacion.as_view(), name='borrar_actualizacion' ),
    # Usuario
    path('juzgado/login/',loginView.as_view(),name='juzgado_login'),
]