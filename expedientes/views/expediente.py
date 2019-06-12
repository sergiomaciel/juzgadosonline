import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import View, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from expedientes.services import expedienteDatoService

class vistaExpediente(View):

   # expediente = expedienteDatoService(User.pk)

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



# class vistaExpediente(TemplateView):

#    template_name = "adminlte/expediente.html"
#    expediente = expedienteDatoService(request.user.id)

#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['expediente'] = expediente.get(1)
#         return context

#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['expediente'] = expediente.get(1)
#         return context        

   # def get(self, request, pk):
   #    expediente = expedienteDatoService(request.user.id)
   #    contexto = expediente.get(pk)
   #    return render(request, "adminlte/expediente.html", contexto)

   # def post(self, request, pk):
   #    expediente = expedienteDatoService(request.user.id)
   #    contexto = expediente.suscripcion()
   #    return render(request, "adminlte/expediente.html", contexto) 
