from django.views.generic import ListView

from expedientes.models import Expediente

class vistaListaExpedientes(ListView):
   model = Expediente
   template_name = 'lista_expedientes.html'
   # template_name = 'adminlte/index.html'



   def get_expedienteComo(self):
      return Expediente.objects.all()[:5]
   # def get_expedientes(self):
   #    return Expediente.objects.all()    