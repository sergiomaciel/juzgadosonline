from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

from juzgados.forms import expedienteForm
from juzgados.services import juzgadoService
from expedientes.services import expedienteService
from expedientes.models import Expediente
from juzgados.models import Delegado

class crearExpediente(View):
   
   def get(self, request):
      
      return render(request, "adminlte/juzgado-CRUD_expediente.html", {})

   def post(self, request):
      form = expedienteForm(request.POST)

      if form.is_valid():
            delegado = Delegado.objects.get(usuario=request.user)
            
            numero = self.request.POST.get('numero')
            actor = self.request.POST.get('actor')
            demandado = self.request.POST.get('demandado')
            causa = self.request.POST.get('causa')
            
            expediente = expedienteService(delegado.usuario, delegado.juzgado)
            expediente.agregar(numero, actor, demandado, causa)
            return HttpResponseRedirect('/juzgado/')
      return render(request, "adminlte/juzgado-CRUD_expediente.html", {})      
         

class actualizarExpediente(View):
   
   def get(self, request, pk):
      expediente = Expediente.objects.get(pk=pk)
      # form = expedienteForm(
      #    initial={
      #       "numero": expediente.numero,
      #       "actor": expediente.actor,
      #       "demandado": expediente.demandado,
      #       "causa": expediente.causa,
      #       })
      
      return render(request, "adminlte/juzgado-CRUD_expediente.html", {
         'expediente': expediente
         })

   def post(self, request, pk):
      form = expedienteForm(request.POST)

      if form.is_valid():
            delegado = Delegado.objects.get(usuario=request.user)
            
            numero = self.request.POST.get('numero')
            actor = self.request.POST.get('actor')
            demandado = self.request.POST.get('demandado')
            causa = self.request.POST.get('causa')
            
            expediente = expedienteService(delegado.usuario, delegado.juzgado)
            expediente.actualizar(numero, actor, demandado, causa)
            return HttpResponseRedirect('/juzgado/')
      return render(request, "adminlte/juzgado-CRUD_expediente.html", {})         