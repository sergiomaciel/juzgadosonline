import datetime
from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import UpdateView

from expedientes.services import serviceExpediente

class vistaExpediente(View):

   __expediente = serviceExpediente()

   def get(self, request, pk):
      contexto = self.__expediente.get(pk, request.user.id)
      return render(request, "adminlte/expediente.html", contexto)

   def post(self, request, pk):
      contexto = self.__expediente.suscripcion()
      return render(request, "adminlte/expediente.html", contexto) 
