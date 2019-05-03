import requests
from django.shortcuts import render
from .models import Despacho
from .services import BuscarDespachos,ExtraerExpedientes,Cargar

#url = "https://old.justiciachaco.gov.ar/listas/C_A_Civ_y_Com_Sala_I_Pro/Cam_Civ_Sala_I_Pro_2019-03-12.Txt"

def list_despachos(request):  
   despacho = Despacho.objects.get(pk=1)
   exps = ExtraerExpedientes()
   exps.procesarDespacho(despacho.url)
   expedientes = exps.procesarExpediente()

   return render(request, 'extractor/lista.html', {'expedientes': expedientes})


def buscar_despachos(request):
   desp = Despacho.objects.get(pk=1)
   B = BuscarDespachos(desp.url)  

   return render(request, 'extractor/buscar.html', {'data':desp, 'despachos': B.despachos})


def cargar(request):
   resultado = Cargar.existeExpediente(2,2)

   return render(request, 'extractor/cargar.html', {'resultado':resultado})


