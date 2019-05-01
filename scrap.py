import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url_root = "https://old.justiciachaco.gov.ar"

def links(url):
   res = requests.get(url).text
   soup = BeautifulSoup(res)
   links = soup.find_all('a')
   links.pop(0)
   return links


def filtrarPro(list_juzgados):
   list_pro = []
   for pro in list_juzgados:
      juz = pro.get('href')
      if juz.find('Pro') >= 0:
         list_pro.append(pro)
   
   list_pro.pop()
   return list_pro


def linkActualizaciones(list_juzgados):
   juzgados = []
   i = 0
   total = len(list_juzgados)
   for link_juz in list_juzgados:
      falta = (total * i)/100
      print( "Progreso: " + str(falta) + '\n' )
      act_juz = links(url_root + link_juz.get('href'))#links de c/d juz
      if len(act_juz) >= 3:
         url_act_juz = act_juz.pop(3).get('href')#Toma el tercer link de
         parte_url  = url_act_juz.split("/")
         
         juzgados.append(
            {  'nombre':parte_url.pop(2),
               'ruta':url_root + url_act_juz[:-14],
            }
         )
      i+=1   
   return juzgados      


scan_pro = False
links_juzs = links(url_root+"/listas")
links_juzs_pro = filtrarPro(links_juzs)

if scan_pro:
   juzgados = linkActualizaciones(links_juzs_pro)
else:
   links_juzs.pop()
   links_juzs.pop()
   links_juzs.pop()
   juzgados = linkActualizaciones(links_juzs)   


archivo = open("./Archivo/juzgados/DEMO.json", "w")
archivo.write('[')
for juzgado in juzgados:
   archivo.write(' {')
   archivo.write("   'ID': 0000"+',\n')
   archivo.write("   'nombre': '"+juzgado['nombre'].strip()+"',\n")
   archivo.write("   'ruta': '"+juzgado['ruta'].strip()+"',\n")
   archivo.write(' },\n')
archivo.write(']')   
archivo.close