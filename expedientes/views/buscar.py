from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from expedientes.forms import buscarExpedienteForm
from expedientes.models import Expediente
from juzgados.services import juzgadoService

class buscarExpediente(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'
   
   def get(self, request):
      form = buscarExpedienteForm()
      return render(request, "adminlte/buscar.html", {'form': form})

   def post(self, request):
      form = buscarExpedienteForm(request.POST)
      expedientes = []
      if form.is_valid():
            juzgado = self.request.POST.get('juzgado')
            numero = self.request.POST.get('numero')
            J = juzgadoService()
            expedientes = J.buscarExpediente(juzgado, numero)
      return render(request, "adminlte/buscar.html", {'form': form, 'expedientes':expedientes})   