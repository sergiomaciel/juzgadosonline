from django.shortcuts import render
from django.views.generic import View

from juzgados.services import juzgadoService

class homeJuzgado(View):
   
   def get(self, request):
      expedientes = juzgadoService()
      return render(request, "adminlte/juzgado-expedientes.html", {
         'expedientes':expedientes.getAllExpediente(1),
         'creados':expedientes.getExpedienteAutor(1, request.user)
         })