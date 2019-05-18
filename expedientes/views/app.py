from django.shortcuts import render
from django.views.generic import View

from expedientes.models import Expediente, Actualizacion

class vistaApp(View):
   
   def get(self, request):
      expedientes= Expediente.objects.all()
      return render(request, "adminlte/index.html", {
         'expediente':expedientes         
         })