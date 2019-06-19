from django.shortcuts import render
from django.views.generic import View

from expedientes.services import MisExpediente
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
class vistaApp(LoginRequiredMixin, View):
   login_url = 'user_login'
   redirect_field_name = 'redirect_to'
   
   def get(self, request):
      expedientes = MisExpediente(request.user)
      return render(request, "adminlte/index.html", {
         'suscriptos':expedientes.novedades(30)
         })