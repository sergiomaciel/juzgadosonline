from django.contrib.auth.models import User
from expedientes.models import Expediente
from juzgados.services import juzgadoService

class buscarService():

   def expediente(self, idJuzgado):
      juzgado = juzgadoService()
      return juzgado.getExpedientes()
