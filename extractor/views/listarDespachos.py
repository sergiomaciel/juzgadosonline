from django.views.generic import ListView

from extractor.models import Despacho

class ListarDespachos(ListView):
   template_name = 'extractor/despachos.html'
   model = Despacho

   def get_lista(self):
      res = Despacho.objects.all()
      return res