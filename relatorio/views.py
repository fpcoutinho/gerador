from threading import local
from django.shortcuts import render

from django.shortcuts import render, redirect
from django import forms
from datetime import datetime
from .models import Relatorio
from . import forms as rel_forms
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/")
def relatorio_list(request):
    usuario = request.user
    if(request.method=='POST'):
        busca = request.POST['busca']
        relatorios = Relatorio.objects.filter(autor=usuario, local__contains=busca).order_by('data')
        return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios, 'busca':busca})
    relatorios = Relatorio.objects.filter(autor=usuario).order_by('data')
    return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios})
    

@login_required(login_url="/accounts/login/")
def relatorio_visualiza(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    now = timezone.now()
    return render(request, 'relatorio/relatorio_visualiza.html', {'relatorio': relatorio})


@login_required(login_url="/accounts/login/")
def relatorio_cria(request):
    if request.method == 'POST':
        form = rel_forms.CriaRelatorioForm(request.POST)
        if form.is_valid():
            usuario = request.user
            relatorios = Relatorio.objects.filter(autor=usuario)
            instance = form.save(commit=False)
            instance.autor = usuario
            instance.save()
            return redirect('relatorio:list')
    else:
        form = rel_forms.CriaRelatorioForm()
    return render(request, 'relatorio/relatorio_cria.html', {'form': form})
    
    
@login_required(login_url="/accounts/login/")
def relatorio_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.EditaRelatorioForm(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
        
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})
    

@login_required(login_url="/accounts/login/")
def relatorio_deleta(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    relatorio.delete()
    messages.success(request, "Relatorio excluído!")
    return redirect('relatorio:list')

@login_required(login_url="/accounts/login/")
def relatorio_exporta(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    return redirect('relatorio:list')
