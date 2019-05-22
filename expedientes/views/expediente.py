from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import UpdateView

from expedientes.models import Expediente, Actualizacion
from expedientes.forms import suscribirseForm

class vistaExpediente(View):

   def get(self, request, pk):
      expediente= Expediente.objects.get(pk=pk)
      actualizaciones= Actualizacion.objects.filter(expediente=pk)
      return render(request, "adminlte/expediente.html", {
         'expediente':expediente,
         'actualizaciones': actualizaciones
         })

class Subscriptores(View):

   def post(self, request, pk):
      expediente = Expediente.objects.get(pk=pk)
      # usuario = User.objects.get(pk=IdUser)
      
      if (request.user in expediente.subscriptores):
         expediente.subscriptores.remove(request.user)
      else:
         expediente.subscriptores.add(request.user)
      
      return render(request, "adminlte/expediente.html", {})