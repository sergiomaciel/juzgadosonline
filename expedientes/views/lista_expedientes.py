from django.views.generic import ListView

from expedientes.models import Expediente

class vistaListaExpedientes(ListView):
   model = Expediente
   template_name = 'lista_expedientes.html'

   def get_expedientes(self):
      return Expediente.objects.all()  