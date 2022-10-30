from tkinter import Widget
from django.db import models
from django.contrib.auth.models import User


class Relatorio(models.Model):

    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    data = models.DateTimeField()
    local = models.CharField(max_length=100)
    temperatura = models.IntegerField()
    clima = models.CharField(max_length=100)
    responsaveis = models.TextField(blank=True)
    Qualificacao_Profissional = models.CharField(max_length=100, default='')
    riscos = models.CharField(max_length=100, default='')
    equipamentos = models.CharField(max_length=100, default='')
    sinalizacao = models.CharField(max_length=100, default='')
    desligamento = models.CharField(max_length=4, default='')
    integridade = models.CharField(max_length=4, default='')
    dialogo = models.CharField(max_length=4, default='')
    curso_nr = models.CharField(max_length=4, default='')
    conferido = models.CharField(max_length=4, default='')
    delimitar_area = models.CharField(max_length=4, default='')
    auxconces = models.CharField(max_length=4, default='')
    tensao = models.CharField(max_length=4, default='')
    aterramento = models.CharField(max_length=4, default='')
    altura = models.CharField(max_length=4, default='')
    cinto_seg = models.CharField(max_length=4, default='')
    requi_seg = models.CharField(max_length=4, default='')
    reavaliacao = models.CharField(max_length=4, default='')
