from juzgados.models import Juzgado
from django.views.generic.list import ListView

class listaJuzgados(ListView):
   template_name = "juzgado/juzgados.html"
   model = Juzgado
   context_object_name = 'juzgados'
   paginate_by = 10  # if pagination is desired

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context