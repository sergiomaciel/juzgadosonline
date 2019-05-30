from juzgados.models import Ciudad
from juzgados.services import provinciaService

class ciudadService():

   def get(self, nombre):
      return Ciudad.objects.get(nombre=nombre)


   def get_provincia(self, nombre):
      provincia = provinciaService()
      return Ciudad.objects.filter(provincia=provincia.get(nombre))   


   def get_all(self):
      return Ciudad.objects.all()
