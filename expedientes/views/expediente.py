import datetime
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.generic import View, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from expedientes.services import expedienteService

class vistaExpediente(View):

   # expediente = expedienteService(User.pk)

   def get(self, request, pk):
      self.expediente = expedienteService(request.user.id)
      contexto = self.expediente.get(pk)
      return render(request, "adminlte/expediente.html", contexto)

   def post(self, request, pk):
      # self.expediente = expedienteService(request.user)
      contexto = self.expediente.suscripcion()
      return render(request, "adminlte/expediente.html", contexto) 



# class vistaExpediente(TemplateView):

#    template_name = "adminlte/expediente.html"
#    expediente = expedienteService(request.user.id)

#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['expediente'] = expediente.get(1)
#         return context

#    def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['expediente'] = expediente.get(1)
#         return context        

   # def get(self, request, pk):
   #    expediente = expedienteService(request.user.id)
   #    contexto = expediente.get(pk)
   #    return render(request, "adminlte/expediente.html", contexto)

   # def post(self, request, pk):
   #    expediente = expedienteService(request.user.id)
   #    contexto = expediente.suscripcion()
   #    return render(request, "adminlte/expediente.html", contexto) 
