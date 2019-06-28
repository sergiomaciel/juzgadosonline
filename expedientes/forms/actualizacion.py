from django import forms
from expedientes.models import Actualizacion


class ActualizacionForm(forms.ModelForm):
     class Meta():
         model = Actualizacion
         fields = ('expediente','tipo','contenido','fecha_creado','fecha_publicado','autor')