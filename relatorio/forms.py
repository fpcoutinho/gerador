from email.policy import default
from django import forms
from . import models
from django.forms.widgets import DateTimeInput, RadioSelect


class CriaRelatorioForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    radio=[('Sim','Sim'), ('Não','Não')]
    quali = [('EE','Engenheiro Eletricista')]
    especialista = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    
    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'temperatura', 'clima', 'responsaveis', 'especialista']
        


class EditaRelatorioForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type': 'datetime-local'}), input_formats='%d/%m/%Y %H:%M')
    radio=[('Sim','Sim'), ('Não','Não')]
    especialista = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)

    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'temperatura', 'clima', 'responsaveis', 'especialista']