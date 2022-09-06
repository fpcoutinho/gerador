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
    relatorios = Relatorio.objects.filter(autor=usuario).order_by('data_inicial')
    return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios})


@login_required(login_url="/accounts/login/")
def relatorio_visualiza(request, comp_id):
    relatorio = Relatorio.objects.get(id=comp_id)
    now = timezone.now()
    return render(request, 'relatorio/relatorio_visualiza.html', {'relatorio': relatorio})


@login_required(login_url="/accounts/login/")
def relatorio_cria(request):
    if request.method == 'POST':
        form = rel_forms.CriaRelatorioForm(request.POST)
        if form.is_valid():
            usuario = request.user
            relatorios = Relatorio.objects.filter(autor=usuario)
            try:
                if(checaData(request, relatorios)):
                    instance = form.save(commit=False)
                instance.autor = usuario
                instance.save()
                return redirect('relatorio:list')
            except forms.ValidationError as e:
                form.add_error('data_final', e.message)
            return render(request, 'relatorio/relatorio_cria.html', {'form':form})
    else:
        form = rel_forms.CriaRelatorioForm()
    return render(request, 'relatorio/relatorio_cria.html', {'form': form})
    
    
@login_required(login_url="/accounts/login/")
def relatorio_edita(request, comp_id):
    relatorio = Relatorio.objects.get(id=comp_id)
    form = rel_forms.EditaRelatorioForm(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=comp_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
        
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})
    

@login_required(login_url="/accounts/login/")
def relatorio_deleta(request, comp_id):
    relatorio = Relatorio.objects.get(id=comp_id)
    relatorio.delete()
    messages.success(request, "Relatorio excluído!")
    return redirect('relatorio:list')
