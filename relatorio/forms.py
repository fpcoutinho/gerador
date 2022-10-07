from email.policy import default
from django import forms
from . import models
from django.forms.widgets import DateTimeInput, RadioSelect, CheckboxSelectMultiple


class CriaRelatorioForm(forms.ModelForm):
    
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')
    clima = forms.CharField(label='Condições Climáticas:')
    temperatura = forms.IntegerField(label='Temperatura (em °C):')

    quali = [('Engenheiro Eletricista','Engenheiro Eletricista'), ('Técnico Eletrotécnico', 'Técnico Eletrotécnico'), ('Eletricista','Eletricista'), ('Aluno de curso profissionalizante', 'Aluno de curso profissionalizante')]
    Qualificacao_Profissional = forms.ChoiceField(choices=quali, widget=forms.RadioSelect, label='Qual a qualificação profissional dos responsáveis pela inspeção?')
    
    radio=[('Sim','Sim'), ('Não','Não')]
    integridade = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Os participantes da inspeção estão bem fisicamente e mentalmente?')
    dialogo = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Houve diálogo de segurança?')
    curso_nr = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Um ou mais executores da inspeção possui curso NR-10?')
    conferido = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='O serviço foi preliminarmente conferido?')
    
    risk = [('Queda','Queda'), ('Explosão', 'Explosão'), ('Ergonômico','Ergonômico'), ('Animais Peçonhentos', 'Animais Peçonhentos'), ('Arco Voltaico','Arco Voltaico'), ('Atropelamento','Atropelamento'), ('Ruído','Ruído'), ('Choque','Choque')]
    riscos = forms.MultipleChoiceField(choices=risk, widget=forms.CheckboxSelectMultiple(), label='Quais riscos foram detectados?')

    eqp = [('Capacete','Capacete'), ('Manga Isolante','Manga Isolante'), ('Botina Dielétrica', 'Botina Dielétrica'), ('Luva de Cobertura','Luva de Cobertura'), ('Óculos de Proteção','Óculos de Proteção'), ('Protetor Auricular','Protetor Auricular'), ('Luva de Borracha Isolante','Luva de Borracha Isolante'), ('Cinto de Segurança','Cinto de Segurança')]
    equipamentos = forms.MultipleChoiceField(choices=eqp, widget=forms.CheckboxSelectMultiple(), label='Quais equipamentos de segurança serão utilizados?')

    desligamento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Este serviço requer desligamento ou bloqueio de equipamento ou rede?')

    silz = [('Cone','Cone'),('Giroflex','Giroflex'),('Fita para Isolamento da área','Fita para Isolamento da área'), ('Sinaleira Sonora','Sinaleira Sonora'), ('Cavaletes','Cavaletes'), ('Nenhum','Nenhum')]
    sinalizacao = forms.MultipleChoiceField(choices=silz, widget=forms.CheckboxSelectMultiple(), label='Este serviço requer sinalização?')

    delimitar_area = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessita delimitar a área de trabalho?')
    auxconces = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessita de auxílio de concessionária local?')
    tensao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessário fazer verificação de tensão?')
    aterramento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='A inspeção requer aterramento temporário?')
    altura = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='A inspeção será realizada em altura?')
    cinto_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Será necessário se aprisionar à escada e utilização de cinto de segurança?')
    requi_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Os requisitos de segurança foram atendidos por todos?')
    reavaliacao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Houve necessidade de reavaliação das inspeções realizadas?')
   
   
    class Meta:
        model = models.Relatorio
        fields = ['data', 'local', 'temperatura', 'clima', 'responsaveis','Qualificacao_Profissional','riscos', 'equipamentos', 'sinalizacao', 'desligamento', 'integridade', 'dialogo', 'curso_nr', 'conferido', 'delimitar_area', 'auxconces', 'tensao', 'aterramento', 'altura', 'cinto_seg', 'requi_seg', 'reavaliacao']
        


class EditaRelatorioForm(forms.ModelForm):

    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')
    clima = forms.CharField(label='Condições Climáticas:')
    temperatura = forms.IntegerField(label='Temperatura (em °C):')

    quali = [('EE','Engenheiro Eletricista'), ('TE', 'Técnico Eletrotécnico'), ('EL','Eletricista'), ('AL', 'Aluno de curso profissionalizante')]
    Qualificacao_Profissional = forms.ChoiceField(choices=quali, widget=forms.RadioSelect, label='Qual a qualificação profissional dos responsáveis pela inspeção?')
    
    radio=[('Sim','Sim'), ('Não','Não')]
    integridade = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Os participantes da inspeção estão bem fisicamente e mentalmente?')
    dialogo = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Houve diálogo de segurança?')
    curso_nr = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Um ou mais executores da inspeção possui curso NR-10?')
    conferido = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='O serviço foi preliminarmente conferido?')
    
    risk = [('QD','Queda'), ('EX', 'Explosão'), ('ER','Ergonômico'), ('AP', 'Animais Peçonhentos'), ('AV','Arco Voltaico'), ('AT','Atropelamento'), ('RU','Ruído'), ('CH','Choque')]
    riscos = forms.MultipleChoiceField(choices=risk, widget=forms.CheckboxSelectMultiple(), label='Quais riscos foram detectados?')

    eqp = [('CP','Capacete'), ('MI','Manga Isolante'), ('BD', 'Botina Dielétrica'), ('LC','Luva de Cobertura'), ('OP','Óculos de Proteção'), ('PA','Protetor Auricular'), ('LB','Luva de Borracha Isolante'), ('CS','Cinto de Segurança')]
    equipamentos = forms.MultipleChoiceField(choices=eqp, widget=forms.CheckboxSelectMultiple(), label='Quais equipamentos de segurança serão utilizados?')

    desligamento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Este serviço requer desligamento ou bloqueio de equipamento ou rede?')

    silz = [('CN','Cone'),('GF','Giroflex'),('FI','Fita para Isolamento da área'), ('SS','Sinaleira Sonora'), ('CV','Cavaletes'), ('NN','Nenhum')]
    sinalizacao = forms.MultipleChoiceField(choices=silz, widget=forms.CheckboxSelectMultiple(), label='Este serviço requer sinalização?')

    delimitar_area = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessita delimitar a área de trabalho?')
    auxconces = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessita de auxílio de concessionária local?')
    tensao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Necessário fazer verificação de tensão?')
    aterramento = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='A inspeção requer aterramento temporário?')
    altura = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='A inspeção será realizada em altura?')
    cinto_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Será necessário se aprisionar à escada e utilização de cinto de segurança?')
    requi_seg = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Os requisitos de segurança foram atendidos por todos?')
    reavaliacao = forms.ChoiceField(choices=radio, widget=forms.RadioSelect, label='Houve necessidade de reavaliação das inspeções realizadas?')

    class Meta:
        model = models.Relatorio
        fields = ['data', 'local', 'temperatura', 'clima', 'responsaveis','Qualificacao_Profissional','riscos', 'equipamentos', 'sinalizacao', 'desligamento', 'integridade', 'dialogo', 'curso_nr', 'conferido', 'delimitar_area', 'auxconces', 'tensao', 'aterramento', 'altura', 'cinto_seg', 'requi_seg', 'reavaliacao']
