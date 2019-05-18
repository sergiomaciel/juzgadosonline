from django.shortcuts import render
from django.views.generic import View

from expedientes.models import Expediente, Actualizacion

class vistaExpediente(View):

   def get(self, request, pk):
      expediente= Expediente.objects.get(pk=pk)
      actualizaciones= Actualizacion.objects.filter(expediente=pk)
      return render(request, "adminlte/expediente.html", {
         'expediente':expediente,
         'actualizaciones': actualizaciones
         })