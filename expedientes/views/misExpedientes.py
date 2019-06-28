from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView
from django.views.generic.edit import (
   CreateView,
   UpdateView,
   DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from expedientes.forms import SubsAgregarForm
from expedientes.services import MisExpediente
from expedientes.models import Expediente


class vistaMisExpedientes(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'
   
   def get(self, request):
      expedientes = MisExpediente(request.user)
      return render(request, "adminlte/mis-expedientes.html", {
         'suscriptos':expedientes.suscriptos(),
         'creados':expedientes.creados()
         })


class crearExpediente(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'
   
   def get(self, request):
      form = SubsAgregarForm()
      return render(request, "adminlte/expedientePreCarga.html", {'form': form})

   def post(self, request):
      form = SubsAgregarForm(request.POST)

      if form.is_valid():
            juzgado = self.request.POST.get('juzgado')
            numero = self.request.POST.get('numero')
            expediente = MisExpediente(request.user)
            expediente.preCargaCrear(juzgado, numero)
            return HttpResponseRedirect('/app/mis-expedientes/')
      return render(request, "adminlte/expedientePreCarga.html", {'form': form})      
         

class actualizarExpediente(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'

   def get(self, request, pk):
      expedientes = MisExpediente(request.user)
      expediente = expedientes.getExpediente(pk)
      form = SubsAgregarForm(
         initial={
            "provincia": expediente.juzgado.ciudad.provincia,
            "ciudad": expediente.juzgado.ciudad,
            "juzgado": expediente.juzgado,
            "numero": expediente.numero,
            })
      
      return render(request, "adminlte/expedientePreCarga.html", {
         'form': form,
         'expediente': expediente
         })

   def post(self, request, pk):
      form = SubsAgregarForm(request.POST)

      if form.is_valid():
            juzgado = self.request.POST.get('juzgado')
            numero = self.request.POST.get('numero')
            expedientes = MisExpediente(request.user)
            expedientes.preCargaActualizar(pk, juzgado, numero)
            expediente = expedientes.getExpediente(pk)
            return HttpResponseRedirect('/app/mis-expedientes/')
      return render(request, "adminlte/expedientePreCarga.html", {
         'form': form,
         'expediente': expediente
         })


class borrarExpediente(LoginRequiredMixin, DeleteView):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'
   model = Expediente
   success_url = reverse_lazy('mis_expedientes')
   template_name = 'adminlte/borrar-expediente.html'