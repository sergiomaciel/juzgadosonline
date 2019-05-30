from django.shortcuts import render
from django.views.generic import View

from expedientes.services import MisExpediente

class vistaApp(View):
   
   def get(self, request):
      expedientes = MisExpediente(request.user)
      return render(request, "adminlte/index.html", {
         'suscriptos':expedientes.novedades(30)
         })