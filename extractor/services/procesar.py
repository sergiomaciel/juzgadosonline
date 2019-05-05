import requests, re
from extractor.models import Plantilla

# Clasifica el despacho en Expediente
# Procesa los expedientes obteniendo sus partes 
class Procesar():
   
   def __init__(self, url, plantilla:Plantilla):
      self.__plantilla = plantilla
      self.__url = url
      self.__contenido = []
      self.expedientes = []

      self.__clasificar()
      self.__procesar() 
   
   # Sustrae el self.__contenido del __plantilla
   # Quieta el encabezado
   # Clasifica el self.__contenido en expedientes(limpiando el primero)
   def __clasificar(self):
      texto = requests.get(self.__url).text[len(self.__plantilla.encabezado):]
      self.__contenido = texto.split(self.__plantilla.separador)
      primero = self.__contenido.pop(0)
      primero_limpio = primero.replace("--","")
      
      if (primero_limpio[0] == "-"):
         primero_limpio = primero_limpio[2:]
      
      self.__contenido.insert(0,primero_limpio)
      return self.__contenido

   #Quita las partes de la CADENA y retorna una cadena limpia
   def __restoCaratula(self, cadena, partes):
      resto = []
      for parte in partes:
         patron = re.compile(parte)
         tupla = patron.subn("<>", cadena)
         cadena = tupla[0].strip()
      
      resto = cadena.split("<>")
      while "" in resto: resto.remove("")   
      return resto 

      
   # Genera el resto_base de las caratulas
   # Quita de la caratula el resto_base
   # Guarda el contenido y las partes del expediente
   def __procesar(self):      
      tipoCaratula = self.__plantilla.tipos_de_caratulas
      patronBase = tipoCaratula.patron
      partesBase = [
         tipoCaratula.numero,
         tipoCaratula.actor,
         tipoCaratula.demandado,
         tipoCaratula.causa,
         ]
      restoBase = self.__restoCaratula(patronBase, partesBase)
      preProcesado = []
      for expediente in self.__contenido:
         
         partesExpediente = self.__restoCaratula(expediente, restoBase)
         if (len(partesExpediente)>3):
            unidad ={
                  'numero':partesExpediente[0],
                  'actor':partesExpediente[1],
                  'demandado':partesExpediente[2],
                  'causa':partesExpediente[3],
                  'contenido':expediente
               }
         else:
            try:
               unidad = {
                     'numero':partesExpediente[0],
                     'actor':partesExpediente[1],
                     'demandado':'',
                     'causa':partesExpediente[2],
                     'contenido':expediente
                  }

            except (IndexError, ValueError):
               unidad = {
                     'numero':partesExpediente[0],
                     'actor':'',
                     'demandado':'',
                     'causa':'',
                     'contenido':expediente
                  }
         
         preProcesado.append(unidad)

      # Unificar Actualizaciones del mismo expediente
      verificados = set()
      for exp in preProcesado:
         numero = exp.get('numero')
         if numero not in verificados:
            verificados.add(numero)
            self.expedientes.append(exp)
         else:
            for exp_base in self.expedientes:
               if (numero == exp_base.get('numero')):
                  exp_base['contenido'] = exp_base['contenido'] +'\n\n'+ " #################### "+'\n\n' + exp['contenido']

        
      return self.expedientes
