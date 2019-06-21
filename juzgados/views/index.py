from django.shortcuts import render
from django.views.generic import View

from juzgados.services import juzgadoService
from juzgados.models import Delegado

class homeJuzgado(View):
   
   def get(self, request):
      expedientes = juzgadoService()
      delegado = Delegado.objects.get(usuario=request.user)
      return render(request, "adminlte/juzgado-expedientes.html", {
         'expedientes':expedientes.getAllExpediente(delegado.juzgado.id),
         'creados':expedientes.getExpedienteAutor(delegado.juzgado.id, delegado.usuario.id)
         })


