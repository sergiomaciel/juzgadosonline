from juzgados.models import Provincia
from juzgados.models import Ciudad

class provinciaService():

   def get(self, id):
      return Provincia.objects.get(pk=id)


   def getCiudades(self, id):
      provincia = self.get(id)
      return Ciudad.objects.filter(provincia=provincia) 


   def getAll(self):
      return Provincia.objects.all()
