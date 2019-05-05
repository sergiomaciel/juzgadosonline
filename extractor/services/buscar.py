import requests
import datetime
from extractor.models import Despacho
from bs4 import BeautifulSoup

# Busca despachosen la web del juzgado
class Buscar():
   #despachos = Despacho.objects.filter(ultima_fecha__lte= timedelta(days=-1))   
   def __init__(self, despacho:Despacho):
     
      self.despachos = []
      self.__nombre_archivo = ""
      self.__url_juzgado = ""
      self.__fecha_desde = despacho.cargar_desde.strftime('%Y-%m-%d')
      self.__fecha_hasta = despacho.cargar_hasta.strftime('%Y-%m-%d')
      
      self.__obtenerDespachos(despacho.url)

   #Con url demo genera la url de juzgado y el archivo
   def __generarUrl(self, url):
      Vurl = url.split("/")
      nombre = Vurl.pop()
      self.__url_juzgado = url.replace(nombre, "")
      self.__nombre_archivo = nombre[:-14]
      return self.__url_juzgado


   def __obtenerDespachos(self, url):
      self.__generarUrl(url)
      #Scanear url_juzgado y extraer los links
      res = requests.get(self.__url_juzgado).text
      soup = BeautifulSoup(res)
      links = soup.find_all('a')
      
      for link in links:
         link = link.get('href')
         nom_fecha_exten = link.split("/").pop()
         nombre = nom_fecha_exten[:-14]
         
         fecha_str = nom_fecha_exten[len(nombre):-4]
         
         try:
            fecha = datetime.datetime.strptime(fecha_str, '%Y-%m-%d')
            fecha = fecha.strftime('%Y-%m-%d')
            if ( self.__fecha_desde <= fecha <= self.__fecha_hasta ):
               # Verifica que el link del archivo sea como el demo
               if (nombre == self.__nombre_archivo):
                  self.despachos.append(
                        {  'url':self.__url_juzgado+nom_fecha_exten,
                           'fecha':fecha,
                        }
                     ) 
         except ValueError:
            pass         

      return self.despachos
