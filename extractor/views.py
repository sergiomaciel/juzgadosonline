import requests
from django.shortcuts import render
from .models import Despacho
from .services import BuscarDespachos,ExtraerExpedientes


def list_despachos(request):
   #ex = BuscarDespachos("https://old.justiciachaco.gov.ar/listas/Saenz_Pena/Cam_Civ_Sal_I_SP/cam_civ_sal_I_SP_Pro_2016-02-02.Txt")
  
   #despachos = requests.get("https://old.justiciachaco.gov.ar/listas/Saenz_Pena/Cam_Civ_Sal_I_SP/cam_civ_sal_I_SP_Pro_2016-02-02.Txt").text
   ##print(despachos)
   despacho = Despacho.objects.get(pk=1)
   exps = ExtraerExpedientes()
   url = "https://old.justiciachaco.gov.ar/listas/C_A_Civ_y_Com_Sala_I_Pro/Cam_Civ_Sala_I_Pro_2019-03-12.Txt"
   expedientes = exps.procesarDespacho(url, despacho.plantilla.encabezado, despacho.plantilla.separador)

   return render(request, 'extractor/lista.html', {'expedientes': expedientes})