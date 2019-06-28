from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import (
   CreateView,
   UpdateView,
   DeleteView
)
from juzgados.forms import actualizacionForm
from juzgados.services import juzgadoService
from expedientes.services import expedienteService, actualizacionService
from expedientes.models import Expediente, Actualizacion
from juzgados.models import Delegado


class crearActualizacion(View):
   
   def get(self, request, pk):
      expediente = Expediente.objects.get(pk=pk)
      return render(request, "juzgado/juzgado-CRUD_actualizacion.html", {'expediente':expediente})

   def post(self, request, pk):
      form = actualizacionForm(request.POST)
      # print(self.request.POST.get('tipo'))
      # print(self.request.POST.get('contenido'))
      if form.is_valid():
         expediente = Expediente.objects.get(pk=pk)
         A = actualizacionService(request.user, expediente)
         A.agregar(self.request.POST.get('contenido'), self.request.POST.get('tipo'))
         return redirect('CRUD_expediente', pk=expediente.pk)
         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      return render(request, "juzgado/juzgado-CRUD_actualizacion.html", {})      
         

class actualizarActualizacion(View):
   
   def get(self, request, id_Act, id_Exp):
      expediente = Expediente.objects.get(pk=id_Exp)
      actualizacion = Actualizacion.objects.get(pk=id_Act)
      return render(request, "juzgado/juzgado-CRUD_actualizacion.html", {
         'expediente': expediente,
         'actualizacion':actualizacion
         })

   def post(self, request, id_Act, id_Exp):
      form = actualizacionForm(request.POST)
      if form.is_valid():
         expediente = Expediente.objects.get(pk=id_Exp)
         actualizacion = actualizacionService(request.user, expediente)
         actualizacion.actualizar(
            id_Act,
            self.request.POST.get('contenido'),
            self.request.POST.get('tipo')
            )
         return redirect('CRUD_expediente', pk=expediente.pk)
      return render(request, "juzgado/juzgado-CRUD_actualizacion.html", {})


class borrarActualizacion(DeleteView):
   model = Actualizacion
   success_url = reverse_lazy('juzgado')
   template_name = ''    