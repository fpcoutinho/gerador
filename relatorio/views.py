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
import os
from io import BytesIO
from django.http import FileResponse
from docxtpl import DocxTemplate



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
        form = rel_forms.FormRelatorioInicial(request.POST)
        if form.is_valid():
            usuario = request.user
            relatorios = Relatorio.objects.filter(autor=usuario)
            instance = form.save(commit=False)
            instance.autor = usuario
            instance.save()
            return redirect('relatorio:list')
    else:
        form = rel_forms.FormRelatorioInicial()
    return render(request, 'relatorio/relatorio_cria.html', {'form': form})
    
@login_required(login_url="/accounts/login/")
def relatorio_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioInicial(request.POST or None, instance=relatorio)
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
    byte_io = BytesIO()
    doc = DocxTemplate("C:\\Users\\fpcou\OneDrive\Documentos\workspace\gerador\\relatorio\\assets\\template.docx")
    context = { 
        'data':relatorio.data.strftime('%d/%m/%Y'),
        'hora':relatorio.data.strftime('%H:%M'),
        'local':relatorio.local,
        'temperatura':relatorio.temperatura,
        'clima':relatorio.clima,
        'responsaveis':relatorio.responsaveis,
        'Qualificacao_Profissional':relatorio.Qualificacao_Profissional, 
        'integridade':relatorio.integridade,
        'dialogo':relatorio.dialogo,
        'curso_nr':relatorio.curso_nr,
        'conferido':relatorio.conferido,
        'riscos':relatorio.riscos,
        'equipamentos':relatorio.equipamentos,
        'desligamento':relatorio.desligamento,
        'sinalizacao':relatorio.sinalizacao,
        'delimitar_area':relatorio.delimitar_area,
        'auxconces':relatorio.auxconces,
        'tensao':relatorio.tensao,
        'aterramento':relatorio.aterramento,
        'altura':relatorio.altura,
        'cinto_seg':relatorio.cinto_seg,
        'requi_seg':relatorio.requi_seg,
        'reavaliacao':relatorio.reavaliacao
    }
    doc.render(context)
    doc.save(byte_io)
    byte_io.seek(0)
    return FileResponse(byte_io, as_attachment=True, filename=f'generated_{rel_id}.docx')

@login_required(login_url="/accounts/login/")
def planejamento_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.conferido != '':
        return render(request, 'relatorio/relatorio_planejamento_visualiza.html', {'relatorio': relatorio})
        
    form = rel_forms.FormRelatorioDePlanejamento(request.POST or None, instance=relatorio)
    if form.is_valid():
            usuario = relatorio.autor
            relatorios = Relatorio.objects.filter(autor=usuario)
            relatorios2 = relatorios.exclude(id=rel_id)
            instance = form.save(commit=False)
            instance.save()
            return redirect('relatorio:visualiza')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def planejamento_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioDePlanejamento(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def externas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.conferido != '':
        return render(request, 'relatorio/relatorio_externas_visualiza.html', {'relatorio': relatorio})
        
    form = rel_forms.FormRelatorioExternas(request.POST or None, instance=relatorio)
    if form.is_valid():
            usuario = relatorio.autor
            relatorios = Relatorio.objects.filter(autor=usuario)
            relatorios2 = relatorios.exclude(id=rel_id)
            instance = form.save(commit=False)
            instance.save()
            return redirect('relatorio:visualiza')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def externas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioExternas(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def qualitativas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.conferido != '':
        return render(request, 'relatorio/relatorio_qualitativas_visualiza.html', {'relatorio': relatorio})
        
    form = rel_forms.FormRelatorioQualitativa(request.POST or None, instance=relatorio)
    if form.is_valid():
            usuario = relatorio.autor
            relatorios = Relatorio.objects.filter(autor=usuario)
            relatorios2 = relatorios.exclude(id=rel_id)
            instance = form.save(commit=False)
            instance.save()
            return redirect('relatorio:visualiza')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def qualitativas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioQualitativa(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def quantitativas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.conferido != '':
        return render(request, 'relatorio/relatorio_quantitativas_visualiza.html', {'relatorio': relatorio})
        
    form = rel_forms.FormRelatorioQuantitativa(request.POST or None, instance=relatorio)
    if form.is_valid():
            usuario = relatorio.autor
            relatorios = Relatorio.objects.filter(autor=usuario)
            relatorios2 = relatorios.exclude(id=rel_id)
            instance = form.save(commit=False)
            instance.save()
            return redirect('relatorio:visualiza')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})

@login_required(login_url="/accounts/login/")
def quantitativas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioQuantitativa(request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        return redirect('relatorio:list')
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form':form})


