from juzgados.models import Juzgado
from juzgados.services import ciudadService

class juzgadoService():

   def get(self, nombre):
      return Juzgado.objects.get(nombre=nombre)


   def get_ciudad(self, nombre):
      ciudad = ciudadService()
      return Juzgado.objects.filter(ciudad=ciudad.get(nombre))   


   def get_all(self):
      return Juzgado.objects.all()
