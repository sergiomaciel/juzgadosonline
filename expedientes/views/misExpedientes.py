from django.shortcuts import render
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
#    template_name = 'adminlte/nuevo-expediente.html'
#    # permission_required = 'people_and_property.can_add_email'

class crearExpediente(FormView):
   template_name = 'adminlte/nuevo-expediente.html'
   form_class = SubsAgregarForm
   success_url = reverse_lazy('mis_expedientes')
   
   def form_valid(self, form):
      juzgado = self.request.POST.get('juzgado')
      numero = self.request.POST.get('numero')
      idAutor = self.request.user
      pass
         

class actualizarExpediente(UpdateView):
   model = Expediente
   success_url = reverse_lazy('mis_expedientes')
   # fields = ['juzgado', 'numero']
   fields = "__all__"
   # template_name_suffix = '_update_form'
   template_name = 'adminlte/actualizar-expediente.html'


class borrarExpediente(DeleteView):
   model = Expediente
   success_url = reverse_lazy('mis_expedientes')
   template_name = 'adminlte/borrar-expediente.html'