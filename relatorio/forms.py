from django import forms
from . import models
from django.forms.widgets import NumberInput, DateTimeInput


class CriaRelatorioForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    
    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'obs']
        


class EditaCompromissoForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type': 'datetime-local'}), input_formats='%d/%m/%Y %H:%M')
    
    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'obs']
        