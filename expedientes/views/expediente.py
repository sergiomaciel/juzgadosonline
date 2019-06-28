import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import View, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from expedientes.services import expedienteDatoService

class vistaExpediente(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'

   def get(self, request, pk):
      E = expedienteDatoService(request.user, pk)
      contexto = {
         'expediente':E.expediente,
         'ultimaActualizacion':E.ultimaActualizacion,
         'suscripto':E.subcripto,
         'actualizaciones': E.actualizaciones,
         'fechas':E.fechas,
         'caducidadad':E.caducidadad
         }
      return render(request, "adminlte/expediente.html", contexto)

   def post(self, request, pk):
      E = expedienteDatoService(request.user, pk)
      E.suscripcion()
      contexto = {
         'expediente':E.expediente,
         'ultimaActualizacion':E.ultimaActualizacion,
         'suscripto':E.subcripto,
         'actualizaciones': E.actualizaciones,
         'fechas':E.fechas,
         'caducidadad':E.caducidadad
         }
      return render(request, "adminlte/expediente.html", contexto) 
