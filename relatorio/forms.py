from email.policy import default
from django import forms
from . import models
from django.forms.widgets import DateTimeInput, RadioSelect, CheckboxSelectMultiple


class CriaRelatorioForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M')
    #conjunto de forms de sim/nao
    radio=[('Sim','Sim'), ('Não','Não')]
    especialista = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    desligamento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    integridade = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    dialogo = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    curso_nr = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    conferido = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    delimitar_area = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    auxconces = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    tensao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    aterramento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    altura = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    cinto_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    requi_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    reavaliacao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    
    quali = [('EE','Engenheiro Eletricista'), ('TE', 'Técnico Eletrotécnico'), ('EL','Eletricista'), ('AL', 'Aluno de curso profissionalizante')]
    Qualificacao_Profissional = forms.ChoiceField(choices=quali, widget=forms.RadioSelect)
   
    #forms de multipla escolha
    risk = [('QD','Queda'), ('EX', 'Explosão'), ('ER','Ergonômico'), ('AP', 'Animais Peçonhentos'), ('AV','Arco Voltaico'), ('AT','Atropelamento'), ('RU','Ruído'), ('CH','Choque')]
    riscos = forms.MultipleChoiceField(choices=risk, widget=forms.CheckboxSelectMultiple())

    eqp = [('CP','Capacete'), ('MI','Manga Isolante'), ('BD', 'Botina Dielétrica'), ('LC','Luva de Cobertura'), ('OP','Óculos de Proteção'), ('PA','Protetor Auricular'), ('LB','Luva de Borracha Isolante'), ('CS','Cinto de Segurança')]
    equipamentos = forms.MultipleChoiceField(choices=eqp, widget=forms.CheckboxSelectMultiple())

    silz = [('CN','Cone'),('GF','Giroflex'),('FI','Fita para Isolamento da área'), ('SS','Sinaleira Sonora'), ('CV','Cavaletes'), ('NN','Nenhum')]
    sinalizacao = forms.MultipleChoiceField(choices=silz, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'temperatura', 'clima', 'responsaveis','Qualificacao_Profissional','riscos', 'equipamentos', 'sinalizacao', 'desligamento', 'especialista', 'integridade', 'dialogo', 'curso_nr', 'conferido', 'delimitar_area', 'auxconces', 'tensao', 'aterramento', 'altura', 'cinto_seg', 'requi_seg', 'reavaliacao']
        


class EditaRelatorioForm(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'type': 'datetime-local'}), input_formats='%d/%m/%Y %H:%M')
    radio=[('Sim','Sim'), ('Não','Não')]
    especialista = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    desligamento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    integridade = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    dialogo = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    curso_nr = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    conferido = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    delimitar_area = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    auxconces = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    tensao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    aterramento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    altura = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    cinto_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    requi_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    reavaliacao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect)
    
    quali = [('EE','Engenheiro Eletricista'), ('TE', 'Técnico Eletrotécnico'), ('EL','Eletricista'), ('AL', 'Aluno de curso profissionalizante')]
    Qualificacao_Profissional = forms.ChoiceField(choices=quali, widget=forms.RadioSelect)

    #forms de multipla escolha
    risk = [('QD','Queda'), ('EX', 'Explosão'), ('ER','Ergonômico'), ('AP', 'Animais Peçonhentos'), ('AV','Arco Voltaico'), ('AT','Atropelamento'), ('RU','Ruído'), ('CH','Choque')]
    riscos = forms.MultipleChoiceField(choices=risk, widget=forms.CheckboxSelectMultiple())

    eqp = [('CP','Capacete'), ('MI','Manga Isolante'), ('BD', 'Botina Dielétrica'), ('LC','Luva de Cobertura'), ('OP','Óculos de Proteção'), ('PA','Protetor Auricular'), ('LB','Luva de Borracha Isolante'), ('CS','Cinto de Segurança')]
    equipamentos = forms.MultipleChoiceField(choices=eqp, widget=forms.CheckboxSelectMultiple())

    silz = [('CN','Cone'),('GF','Giroflex'),('FI','Fita para Isolamento da área'), ('SS','Sinaleira Sonora'), ('CV','Cavaletes'), ('NN','Nenhum')]
    sinalizacao = forms.MultipleChoiceField(choices=silz, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = models.Relatorio
        fields = ['nome', 'local', 'data', 'temperatura', 'clima', 'responsaveis','Qualificacao_Profissional','riscos', 'equipamentos', 'sinalizacao', 'desligamento', 'especialista', 'integridade', 'dialogo', 'curso_nr', 'conferido', 'delimitar_area', 'auxconces', 'tensao', 'aterramento', 'altura', 'cinto_seg', 'requi_seg', 'reavaliacao']
