from http.client import HTTPResponse
from threading import local
from django.shortcuts import render
from django.shortcuts import render, redirect
from django import forms
from datetime import datetime
from .models import Relatorio, Circuito, Imagens
from . import forms as rel_forms
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import os
from io import BytesIO
import cloudinary
import zipfile
import requests
import urllib.request
from django.http import FileResponse
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm
import ast
from django.conf import settings


@login_required(login_url="/accounts/login/")
def relatorio_list(request):
    usuario = request.user
    if (request.method == 'POST'):
        busca = request.POST['busca']
        relatorios = Relatorio.objects.filter(
            autor=usuario, local__contains=busca).order_by('data')
        return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios, 'busca': busca})
    relatorios = Relatorio.objects.filter(autor=usuario).order_by('data')
    return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios})


@login_required(login_url="/accounts/login/")
def relatorio_visualiza(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    imagens = Imagens.objects.filter(rel_pai__pk=rel_id)
    now = timezone.now()
    return render(request, 'relatorio/relatorio_visualiza.html', {'relatorio': relatorio, 'imagens': imagens})


@login_required(login_url="/accounts/login/")
def relatorio_cria(request):
    if request.method == 'POST':
        form = rel_forms.FormRelatorioInicial(request.POST)
        if form.is_valid():
            usuario = request.user
            relatorios = Relatorio.objects.filter(autor=usuario)
            bloco = form.cleaned_data.get('local').split('-')
            bloco = bloco[0]
            relatorios2 = relatorios.filter(local__contains=bloco)
            instance = form.save(commit=False)
            if relatorios2:
                instance.qualiprof = relatorios2[0].qualiprof
                instance.integridade = relatorios2[0].integridade
                instance.dialogo = relatorios2[0].dialogo
                instance.curso_nr = relatorios2[0].curso_nr
                instance.conferido = relatorios2[0].conferido
                instance.riscos = relatorios2[0].riscos
                instance.equipamentos = relatorios2[0].equipamentos
                instance.desligamento = relatorios2[0].desligamento
                instance.sinalizacao = relatorios2[0].sinalizacao
                instance.delimitar_area = relatorios2[0].delimitar_area
                instance.auxconces = relatorios2[0].auxconces
                instance.tensao = relatorios2[0].tensao
                instance.aterramento = relatorios2[0].aterramento
                instance.altura = relatorios2[0].altura
                instance.cinto_seg = relatorios2[0].cinto_seg
                instance.requi_seg = relatorios2[0].requi_seg
                instance.reavaliacao = relatorios2[0].reavaliacao
            instance.autor = usuario
            instance.save()
            imagens = request.FILES.getlist('imagens[]')
            for imagem in imagens:
                instance_img = Imagens(rel_pai=instance, img=imagem)
                instance_img.save()
            return redirect('relatorio:visualiza', instance.id)
    else:
        form = rel_forms.FormRelatorioInicial()
    return render(request, 'relatorio/relatorio_cria.html', {'form': form})


@login_required(login_url="/accounts/login/")
def relatorio_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioInicial(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()
        return redirect('relatorio:visualiza', instance.id)

    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def relatorio_deleta(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    relatorio.delete()
    messages.success(request, "Relatorio excluído!")
    return redirect('relatorio:list')


@login_required(login_url="/accounts/login/")
def relatorio_exporta(request, rel_id):
    # sourcery skip: simplify-dictionary-update, use-fstring-for-concatenation
    relatorio = Relatorio.objects.get(id=rel_id)
    circuitos = Circuito.objects.filter(rel_pai__pk=rel_id)
    imagens = Imagens.objects.filter(rel_pai__pk=rel_id)
    byte_io = BytesIO()
    base = settings.PROJECT_PATH
    media = settings.MEDIA_ROOT + settings.MEDIA_URL
    doc = DocxTemplate(os.path.join(base, "relatorio/assets/template.docx"))
    context = {
        'data': relatorio.data.strftime('%d/%m/%Y'),
        'hora': relatorio.data.strftime('%H:%M'),
        'local': relatorio.local,
        'temperatura': relatorio.temperatura,
        'clima': relatorio.clima,
        'responsaveis': relatorio.responsaveis,
        'qualiprof': relatorio.qualiprof,
        'integridade': relatorio.integridade,
        'dialogo': relatorio.dialogo,
        'curso_nr': relatorio.curso_nr,
        'conferido': relatorio.conferido,
        'riscos': ', '.join(ast.literal_eval(relatorio.riscos)),
        'equipamentos': ', '.join(ast.literal_eval(relatorio.equipamentos)),
        'desligamento': relatorio.desligamento,
        'sinalizacao': ', '.join(ast.literal_eval(relatorio.sinalizacao)),
        'delimitar_area': relatorio.delimitar_area,
        'auxconces': relatorio.auxconces,
        'tensao': relatorio.tensao,
        'aterramento': relatorio.aterramento,
        'altura': relatorio.altura,
        'cinto_seg': relatorio.cinto_seg,
        'requi_seg': relatorio.requi_seg,
        'reavaliacao': relatorio.reavaliacao,
        'tempambiente': relatorio.tempambiente,
        'condambiente': relatorio.condambiente,
        'altitude': relatorio.altitude,
        'presagua': relatorio.presagua,
        'pressolidos': relatorio.pressolidos,
        'pressubst': relatorio.pressubst,
        'solmecanicas': relatorio.solmecanicas,
        'presmofo': relatorio.presmofo,
        'presfauna': relatorio.presfauna,
        'infleletro': relatorio.infleletro,
        'radsolar': relatorio.radsolar,
        'descatm': relatorio.descatm,
        'movdoar': relatorio.movdoar,
        'vento': relatorio.vento,
        'competencia': relatorio.competencia,
        'reseletr': relatorio.reseletr,
        'contpessoas': relatorio.contpessoas,
        'condfuga': relatorio.condfuga,
        'natmatpr': relatorio.natmatpr,
        'natmatcons': relatorio.natmatcons,
        'classestr': relatorio.classestr,
        'documentacao': relatorio.documentacao.split(': '),
        'ambientesofreu': relatorio.ambientesofreu.split(': '),
        'instalacaoinspecionada': relatorio.instalacaoinspecionada.split(': '),
        'linhaseletricasdisp': relatorio.linhaseletricasdisp.split(': '),
        'compinstalacao': relatorio.compinstalacao.split(': '),
        'linhaseletricascorr': relatorio.linhaseletricascorr.split(': '),
        'tomadasdeforca': relatorio.tomadasdeforca.split(': '),
        'qtdesufitomadas': relatorio.qtdesufitomadas.split(': '),
        'instlquadist': relatorio.instlquadist.split(': '),
        'novoscircuitos': relatorio.novoscircuitos,
        'advquadist': relatorio.advquadist.split(': '),
        'dispprotecaoident': relatorio.dispprotecaoident.split(': '),
        'protcircuitos': relatorio.protcircuitos.split(': '),
        'barramentoquadist': relatorio.barramentoquadist.split(': '),
        'bitola': relatorio.bitola.split(': '),
        'condutident': relatorio.condutident.split(': '),
        'disjundif': relatorio.disjundif.split(': '),
        'dispprotecaosurtos': relatorio.dispprotecaosurtos.split(': '),
        'servseguranca': relatorio.servseguranca.split(': '),
        'esqaterramento': relatorio.esqaterramento,
        'reservadeenergia': relatorio.reservadeenergia.split(': '),
        'fontseguranca': relatorio.fontseguranca.split(': '),
        'paralelismo': relatorio.paralelismo.split(': '),
        'capbarramento': relatorio.capbarramento,
        'protgeral': relatorio.protgeral,
        'protdr': relatorio.protdr,
        'protdps': relatorio.protdps,
        'vab': relatorio.vab,
        'van': relatorio.van,
        'ia': relatorio.ia,
        'vbc': relatorio.vbc,
        'vbn': relatorio.vbn,
        'ib': relatorio.ib,
        'vca': relatorio.vca,
        'vcn': relatorio.vcn,
        'ic': relatorio.ic,
        'continuidade': relatorio.continuidade.split(': '),
        'resistencia': relatorio.resistencia.split(': '),
        'selvpelv': relatorio.selvpelv.split(': '),
        'verificacao': relatorio.verificacao.split(': '),
        'ensaiodetensao': relatorio.ensaiodetensao.split(': '),
        'ensaiodefunc': relatorio.ensaiodefunc.split(': '),
    }

    for i in range(len(circuitos)):
        numero = str(i)
        context.update({('circuito'+numero): circuitos[i].modelo})
        context.update({('fase'+numero): circuitos[i].fase})
        context.update({('disjuntor'+numero): circuitos[i].disjuntor})
        context.update({('descricao'+numero): circuitos[i].descricao})
        context.update({('condutor'+numero): circuitos[i].condutor})
        context.update({('corrente'+numero): circuitos[i].corrente})

    fotos = []
    for i in imagens:
        img_id = ((i.img.url).split('/')[-1]).split('.')[0]
        diretorio = media + (i.img.url).split('/')[-1]
        down_url = cloudinary.utils.cloudinary_url(img_id)[0]
        urllib.request.urlretrieve(down_url, diretorio)
        fotos.append(InlineImage(doc, diretorio, width=Mm(50)))

    context.update({'imagens': fotos})

    doc.render(context)
    doc.save(byte_io)
    byte_io.seek(0)
    return FileResponse(byte_io, as_attachment=True, filename=f'relatório_{relatorio.local}.docx')


@login_required(login_url="/accounts/login/")
def download_imagens(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    imagens = Imagens.objects.filter(rel_pai__pk=rel_id)
    buffer = BytesIO()
    zip_file = zipfile.ZipFile(buffer, 'w')
    for i in imagens:
        imagem = requests.get(i.img.url)
        filename = (i.img.url).split('/')[-1]
        zip_file.writestr(filename, imagem.content)
    zip_file.close()
    buffer.seek(0)

    return FileResponse(buffer, as_attachment=True, filename=f'imagens_{relatorio.local}.zip')


@login_required(login_url="/accounts/login/")
def planejamento_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.qualiprof != '':
        return render(request, 'relatorio/relatorio_planejamento_visualiza.html', {'relatorio': relatorio})

    form = rel_forms.FormRelatorioDePlanejamento(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()
        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def planejamento_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioDePlanejamento(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()
        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def externas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.tempambiente != '':
        return render(request, 'relatorio/relatorio_externas_visualiza.html', {'relatorio': relatorio})

    form = rel_forms.FormRelatorioExternas(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()

        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def externas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioExternas(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()

        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def qualitativas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    if relatorio.documentacao != '':
        return render(request, 'relatorio/relatorio_qualitativas_visualiza.html', {'relatorio': relatorio})

    form = rel_forms.FormRelatorioQualitativa(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()

        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def qualitativas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioQualitativa(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()

        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def quantitativas_add(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    circuitos = Circuito.objects.filter(rel_pai__pk=rel_id)
    if relatorio.continuidade != '':
        return render(request, 'relatorio/relatorio_quantitativas_visualiza.html', {'relatorio': relatorio, 'circuitos': circuitos})

    form = rel_forms.FormRelatorioQuantitativa(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()
        return redirect('relatorio:visualiza', rel_id)

    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def quantitativas_edita(request, rel_id):
    relatorio = Relatorio.objects.get(id=rel_id)
    form = rel_forms.FormRelatorioQuantitativa(
        request.POST or None, instance=relatorio)
    if form.is_valid():
        usuario = relatorio.autor
        relatorios = Relatorio.objects.filter(autor=usuario)
        relatorios2 = relatorios.exclude(id=rel_id)
        instance = form.save(commit=False)
        instance.save()
        imagens = request.FILES.getlist('imagens[]')
        for imagem in imagens:
            instance_img = Imagens(rel_pai=instance, img=imagem)
            instance_img.save()
        return redirect('relatorio:visualiza', rel_id)
    return render(request, 'relatorio/relatorio_edita.html', {'relatorio': relatorio,  'form': form})


@login_required(login_url="/accounts/login/")
def circuito_add(request, rel_id):
    form = rel_forms.FormCircuito(request.POST or None)
    relatorio = Relatorio.objects.get(id=rel_id)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.rel_pai = relatorio
        instance.save()
        return redirect('relatorio:visualiza', rel_id)

    return render(request, 'relatorio/circuito_add.html', {'form': form, 'rel_pai': rel_id})
