from tkinter import Widget
from django.db import models
from django.contrib.auth.models import User


class Relatorio(models.Model):

    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.DateTimeField()
    temperatura = models.IntegerField()
    clima = models.CharField(max_length=100)
    responsaveis = models.TextField(blank=True)
    Qualificacao_Profissional = models.CharField(max_length=100, default="Sim")
    riscos = models.CharField(max_length=100, default="Sim")
    equipamentos = models.CharField(max_length=100, default="Sim")
    sinalizacao = models.CharField(max_length=100, default="Sim")
    desligamento = models.CharField(max_length=4, default="Sim")
    especialista = models.CharField(max_length=4, default="Sim")
    integridade = models.CharField(max_length=4, default="Sim")
    dialogo = models.CharField(max_length=4, default="Sim")
    curso_nr = models.CharField(max_length=4, default="Sim")
    conferido = models.CharField(max_length=4, default="Sim")
    delimitar_area = models.CharField(max_length=4, default="Sim")
    auxconces = models.CharField(max_length=4, default="Sim")
    tensao = models.CharField(max_length=4, default="Sim")
    aterramento = models.CharField(max_length=4, default="Sim")
    altura = models.CharField(max_length=4, default="Sim")
    cinto_seg = models.CharField(max_length=4, default="Sim")
    requi_seg = models.CharField(max_length=4, default="Sim")
    reavaliacao = models.CharField(max_length=4, default="Sim")

    def __str__(self):
        return self.nome
