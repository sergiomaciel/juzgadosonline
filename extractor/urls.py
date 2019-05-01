from django.urls import path
from . import views

urlpatterns = [
    path('extractor/', views.list_despachos),
]