from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from juzgados.services import juzgadoService
from juzgados.models import Delegado

class homeJuzgado(LoginRequiredMixin, View):
   login_url = 'juzgado_login'
   redirect_field_name = 'redirect_to'
   
   def get(self, request):
      try:
         expedientes = juzgadoService()
         delegado = Delegado.objects.get(usuario=request.user)
         return render(request, "juzgado/juzgado-expedientes.html", {
         'expedientes':expedientes.getAllExpediente(delegado.juzgado.id),
         'creados':expedientes.getExpedienteAutor(delegado.juzgado.id, delegado.usuario.id)
         })
      except ObjectDoesNotExist:
         return HttpResponseRedirect('/app/')
      



