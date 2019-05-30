from juzgados.models import Provincia

class provinciaService():

   def get(self, nombre):
      return Provincia.objects.get(nombre=nombre)

   def get_all(self):
      return Provincia.objects.all()
