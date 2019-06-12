from juzgados.models import Juzgado
from expedientes.models import Expediente

class juzgadoService():

   def get(self, id):
      return Juzgado.objects.get(pk=id)


   def getExpedientes(self,id):
      juzgado = self.get(id)
      return Expediente.objects.filter(juzgado=juzgado)


   def getAll(self):
      return Juzgado.objects.all()


   def TotalExpedientes(self):
      pass

   def UltimaActualizacion(self):
      pass   
