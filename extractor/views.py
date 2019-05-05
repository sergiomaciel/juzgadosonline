import requests
from django.shortcuts import render
from .models import Despacho
from .services import Buscar,Procesar,Cargar

#url = "https://old.justiciachaco.gov.ar/listas/C_A_Civ_y_Com_Sala_I_Pro/Cam_Civ_Sala_I_Pro_2019-03-12.Txt"

def buscar_despachos(request):
   desp = Despacho.objects.get(pk=1)
   despachosPendientes = Buscar(desp).despachos
   return render(request, 'extractor/buscar.html', {'data':desp, 'despachos': despachosPendientes})


def list_despachos(request):  
   desp = Despacho.objects.get(pk=1)
   despachosPendientes = Buscar(desp).despachos
   all_expedientes = []
   for despacho in despachosPendientes:
      expedientes = Procesar(despacho.get('url'), desp.plantilla).expedientes      
      for e in expedientes:
         e.update({'fecha':despacho.get('fecha')})
         all_expedientes.append(e)
   
   return render(request, 'extractor/lista.html', {'expedientes': all_expedientes})


def cargar(request):
   despacho = Despacho.objects.get(pk=1)
   url = despacho.url
   ultimaFecha = despacho.ultima_fecha
   despachosSinProcesar = Buscar(despacho).despachos

   resultado = Cargar.existeExpediente(2,2)

   return render(request, 'extractor/cargar.html', {'resultado':resultado})


