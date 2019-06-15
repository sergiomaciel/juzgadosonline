from django import forms
from django_select2.forms import Select2MultipleWidget, ModelSelect2Widget
from django.contrib.auth.models import User
from juzgados.models import Juzgado, Ciudad, Provincia
from expedientes.models import Expediente

class buscarExpedienteForm(forms.Form):

   provincia = forms.ModelChoiceField(
        queryset=Provincia.objects.all(),
      #   empty_label="Seleccione una Provincia",
        label='Provincia',
        widget=ModelSelect2Widget(
            model=Provincia,
            search_fields=['nombre__icontains'],
            dependent_fields={'ciudad': 'ciudad'},
            attrs={'data-placeholder': 'Seleccione una Provincia', 'data-width': '100%'}
        ),
    )

   ciudad = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        label="Ciudad",
        widget=ModelSelect2Widget(
            model=Ciudad,
            search_fields=['nombre__icontains'],
            dependent_fields={'provincia': 'provincia'},
            max_results=500,
            attrs={'data-placeholder': 'Seleccione una Ciudad', 'data-width': '100%'}
        )
   )

   juzgado = forms.ModelChoiceField(
        queryset=Juzgado.objects.all(),
        label="Juzgado",
        widget=ModelSelect2Widget(
            model=Juzgado,
            search_fields=['nombre__icontains'],
            dependent_fields={'ciudad': 'ciudad'},
            attrs={'data-placeholder': 'Seleccione un Juzgado', 'data-width': '100%'}
        )
    )
   # juzgado = forms.ModelChoiceField(queryset=Juzgado.objects.all())
   numero = forms.CharField(initial='000/00')