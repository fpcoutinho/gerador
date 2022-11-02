from tkinter import Widget
from django.db import models
from django.contrib.auth.models import User


class Relatorio(models.Model):

    # Campos principais do relatório.
    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    data = models.DateTimeField()
    local = models.CharField(max_length=100)
    temperatura = models.IntegerField()
    clima = models.CharField(max_length=100)
    responsaveis = models.TextField(blank=True)

    # Campos da Avaliação e planejamento da execução.
    qualiprof = models.CharField(max_length=100, default='')
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


    # Campos da Avaliação das influencias externas da instalação elétrica.
    tempambiente = models.CharField(max_length=30, default='')
    condambiente = models.CharField(max_length=30, default='')
    altitude = models.CharField(max_length=30, default='')
    presagua = models.CharField(max_length=30, default='')
    pressolidos = models.CharField(max_length=30, default='')
    pressubst = models.CharField(max_length=30, default='')
    solmecanicas = models.CharField(max_length=30, default='')
    presmofo = models.CharField(max_length=30, default='')
    presfauna = models.CharField(max_length=30, default='')
    infleletro = models.CharField(max_length=30, default='')
    radsolar = models.CharField(max_length=30, default='')
    descatm = models.CharField(max_length=30, default='')
    movdoar = models.CharField(max_length=30, default='')
    vento = models.CharField(max_length=30, default='')
    competencia = models.CharField(max_length=30, default='')
    reseletr = models.CharField(max_length=30, default='')
    contpessoas = models.CharField(max_length=30, default='')
    condfuga = models.CharField(max_length=30, default='')
    natmatpr = models.CharField(max_length=30, default='')
    natmatcons = models.CharField(max_length=30, default='')
    classestr = models.CharField(max_length=30, default='')

    # Campos da Avaliação qualitativa da instalação elétrica.


    # Campos da Avaliação quantitativa da instalação elétrica.
