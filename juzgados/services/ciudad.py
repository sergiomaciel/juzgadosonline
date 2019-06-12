from juzgados.models import Ciudad
from juzgados.models import Juzgado

class ciudadService():

   def get(self, id):
      return Ciudad.objects.get(pk=id)


   def getJuzgados(self, id):
      ciudad = self.get(id)
      return Juzgado.objects.filter(ciudad=ciudad)   


   def getAll(self):
      return Ciudad.objects.all()
