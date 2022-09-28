from tkinter import Widget
from django.db import models
from django.contrib.auth.models import User


class Relatorio(models.Model):

    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    data = models.DateTimeField()
    temperatura = models.IntegerField()
    clima = models.CharField(max_length=100)
    responsaveis = models.TextField(blank=True)
    especialista = models.CharField(max_length=4, default="Sim")
    autor = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
