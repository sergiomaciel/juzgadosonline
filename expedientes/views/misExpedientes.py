from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View,FormView
from django.views.generic.edit import (
   CreateView,
   UpdateView,
   DeleteView
)
from expedientes.forms import SubsAgregarForm
from expedientes.services import MisExpediente
from expedientes.models import Expediente

class vistaMisExpedientes(View):
   
   def get(self, request):
      expedientes = MisExpediente(request.user)
      return render(request, "adminlte/mis-expedientes.html", {
         'suscriptos':expedientes.suscriptos(),
         'creados':expedientes.creados()
         })


# class crearExpediente(CreateView):
#    model = Expediente
#    success_url = reverse_lazy('mis_expedientes')
#    # fields = ['juzgado', 'numero']
#    fields = "__all__"
#    template_name = 'adminlte/expedientePreCarga.html'
#    # permission_required = 'people_and_property.can_add_email'

# usar selec2

class crearExpediente(View):
   
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
         

class actualizarExpediente(View):
   
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
# class actualizarExpediente(UpdateView):
#    model = Expediente
#    form_class = SubsAgregarForm
#    success_url = reverse_lazy('mis_expedientes')
#    # fields = ['juzgado', 'numero']
#    # fields = "__all__"
#    # template_name_suffix = '_update_form'
#    template_name = 'adminlte/expedientePreCarga.html'
 
#    def get_object(self, queryset=None):
#       obj, created = None
#       # obj, created = MyModel.objects.get_or_create(col_1=self.kwargs['value_1'], col_2=self.kwargs['value_2'])

#       return obj


class borrarExpediente(DeleteView):
   model = Expediente
   success_url = reverse_lazy('mis_expedientes')
   template_name = 'adminlte/borrar-expediente.html'