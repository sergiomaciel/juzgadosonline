import requests, re
import unicodedata
import codecs
import sys
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
   
   def doubledecode(self, s, as_unicode=True):
      cp1252 = {
         # from http://www.microsoft.com/typography/unicode/1252.htm
         u"\u20AC": u"\x80", # EURO SIGN
         u"\u201A": u"\x82", # SINGLE LOW-9 QUOTATION MARK
         u"\u0192": u"\x83", # LATIN SMALL LETTER F WITH HOOK
         u"\u201E": u"\x84", # DOUBLE LOW-9 QUOTATION MARK
         u"\u2026": u"\x85", # HORIZONTAL ELLIPSIS
         u"\u2020": u"\x86", # DAGGER
         u"\u2021": u"\x87", # DOUBLE DAGGER
         u"\u02C6": u"\x88", # MODIFIER LETTER CIRCUMFLEX ACCENT
         u"\u2030": u"\x89", # PER MILLE SIGN
         u"\u0160": u"\x8A", # LATIN CAPITAL LETTER S WITH CARON
         u"\u2039": u"\x8B", # SINGLE LEFT-POINTING ANGLE QUOTATION MARK
         u"\u0152": u"\x8C", # LATIN CAPITAL LIGATURE OE
         u"\u017D": u"\x8E", # LATIN CAPITAL LETTER Z WITH CARON
         u"\u2018": u"\x91", # LEFT SINGLE QUOTATION MARK
         u"\u2019": u"\x92", # RIGHT SINGLE QUOTATION MARK
         u"\u201C": u"\x93", # LEFT DOUBLE QUOTATION MARK
         u"\u201D": u"\x94", # RIGHT DOUBLE QUOTATION MARK
         u"\u2022": u"\x95", # BULLET
         u"\u2013": u"\x96", # EN DASH
         u"\u2014": u"\x97", # EM DASH
         u"\u02DC": u"\x98", # SMALL TILDE
         u"\u2122": u"\x99", # TRADE MARK SIGN
         u"\u0161": u"\x9A", # LATIN SMALL LETTER S WITH CARON
         u"\u203A": u"\x9B", # SINGLE RIGHT-POINTING ANGLE QUOTATION MARK
         u"\u0153": u"\x9C", # LATIN SMALL LIGATURE OE
         u"\u017E": u"\x9E", # LATIN SMALL LETTER Z WITH CARON
         u"\u0178": u"\x9F", # LATIN CAPITAL LETTER Y WITH DIAERESIS
      }
      s = s.encode('utf-8').decode('cp1252') 
      # remove the windows gremlins O^1
      for src, dest in cp1252.items():
         s = s.replace(src, dest)
      s = s.encode('raw_unicode_escape')
      if as_unicode:
         # return as unicode string
         s = s.decode('utf8', 'ignore')
      return s
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

   def resto(self, cadena, partes):
      resto = []
      for parte in partes:
         pos = cadena.find(parte)
         if ((pos != -1) and (parte.strip() != "")):
            R = cadena[0:pos]
            resto.append(R.strip())
            cadena = cadena[pos+len(parte):]
      resto.append(cadena)
      while "" in resto: resto.remove("")   
      return resto
  

   def __caratula(self, cadena, regex):
      partes = []
      # Quita doble espacio en blanco
      cadena = ' '.join(cadena.split())
      # regex = "([0-9]*/[0-9]*.*?\s)(?:\s*-Foja:.*?-)(.*?C/)(.*?S/)(.*?\s?-)"
      
      patron = re.compile(regex)
      # cadena = str.encode(cadena, 'cp1252')
      # cadena = str.encode(cadena, 'utf-8')
      # cadena = codecs.encode(cadena, 'utf-8')    
      
      matches = patron.search(cadena)     
      # Falta contemplar el caso de expediente sin demandado
      if matches:
         partes = list(matches.groups())
      else:
         partes = [1,1,1,1]

      return partes

      
   # Genera el resto_base de las caratulas
   # Quita de la caratula el resto_base
   # Guarda el contenido y las partes del expediente
   def __procesar(self):      
      tipoCaratula = self.__plantilla.tipos_de_caratulas
      patronBase = tipoCaratula.patron
      print(patronBase)
      partesBase = [
         tipoCaratula.numero,
         tipoCaratula.actor,
         tipoCaratula.demandado,
         tipoCaratula.causa,
         ]
      restoBase = self.__restoCaratula(patronBase, partesBase)
      preProcesado = []
      for expediente in self.__contenido:
         # expediente = str(str.decode(expediente, 'cp1252'))
         # expediente = expediente.encode('latin1').decode('windows-1252')
         # expediente = str(str.encode(expediente, 'utf-8'))  

         expediente = self.doubledecode(expediente,True)
         # print(expediente)
         # pastes = self.__restoCaratula(expediente, restoBase)
         pastes = self.__caratula(expediente, patronBase)
         if (len(pastes)>3):
            try:
               unidad ={
                  'numero':pastes[0],
                  'actor':pastes[1],
                  'demandado':pastes[2],
                  'causa':pastes[3],
                  'contenido':expediente
               }
            except (IndexError, ValueError):
               pass
         else:
            try:
               unidad = {
                     'numero':pastes[0],
                     'actor':pastes[1],
                     'demandado':'',
                     'causa':pastes[2],
                     'contenido':expediente
                  }

            except (IndexError, ValueError):
               unidad = {
                     'numero':pastes[0],
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
