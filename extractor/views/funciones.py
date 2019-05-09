import requests
from django.shortcuts import render
from extractor.models import Despacho
from extractor.services import Buscar,Procesar,Cargar

#url = "https://old.justiciachaco.gov.ar/listas/C_A_Civ_y_Com_Sala_I_Pro/Cam_Civ_Sala_I_Pro_2019-03-12.Txt"

def buscar_despachos(request):  
   desp = Despacho.objects.get(pk=1)
   despachosPendientes = Buscar(desp).despachos
   all_expedientes = []
   for despacho in despachosPendientes:
      expedientes = Procesar(despacho.get('url'), desp.plantilla).expedientes      
      for e in expedientes:
         e.update({'fecha_publicado':despacho.get('fecha')})
         all_expedientes.append(e)
   
   return render(request, 'extractor/buscar.html', {'expedientes': all_expedientes})


def cargar(request):
   desp = Despacho.objects.get(pk=1)
   despachosPendientes = Buscar(desp).despachos
   all_expedientes = []
   for despacho in despachosPendientes:
      expedientes = Procesar(despacho.get('url'), desp.plantilla).expedientes      
      for e in expedientes:
         e.update({'fecha_publicado':despacho.get('fecha')})
         all_expedientes.append(e)
         cargarJuzgado = Cargar(desp.juzgado)
         # cargarJuzgado.agregar(e)
         cargarJuzgado.actualizarExpediente(e)

   return render(request, 'extractor/cargar.html', {'expedientes': all_expedientes})


