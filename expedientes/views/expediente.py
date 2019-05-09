from django.shortcuts import render
from django.views.generic import View


from expedientes.models import Expediente

class vistaExpediente(View):

   def get(self, request, pk):
      expediente= Expediente.objects.get(pk=pk)
      return render(request, "expediente.html", {'expediente':expediente})