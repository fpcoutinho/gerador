from email.policy import default
from django import forms
from . import models
from django.forms.widgets import DateTimeInput, RadioSelect, CheckboxSelectMultiple


# Cria e Edita o relatório inicial, apenas com dados simples.
class FormRelatorioInicial(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')
    clima = forms.CharField(label='Condições Climáticas:')
    temperatura = forms.IntegerField(label='Temperatura (em °C):')

    class Meta:
        model = models.Relatorio
        fields = ['data', 'local', 'temperatura', 'clima', 'responsaveis']
        
# Avaliação e planejamento da execução.
class FormRelatorioDePlanejamento(forms.ModelForm):
    quali = [('Engenheiro Eletricista','Engenheiro Eletricista'), ('Técnico Eletrotécnico', 'Técnico Eletrotécnico'), ('Eletricista','Eletricista'), ('Aluno de curso profissionalizante', 'Aluno de curso profissionalizante')]
    qualiprof = forms.ChoiceField(choices=quali, widget=forms.RadioSelect, label='Qual a qualificação profissional dos responsáveis pela inspeção?')
    
    simounao=[('Sim','Sim'), ('Não','Não')]
    integridade = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Os participantes da inspeção estão bem fisicamente e mentalmente?')
    dialogo = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Houve diálogo de segurança?')
    curso_nr = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Um ou mais executores da inspeção possui curso NR-10?')
    conferido = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='O serviço foi preliminarmente conferido?')
    
    risk = [('Queda','Queda'), ('Explosão', 'Explosão'), ('Ergonômico','Ergonômico'), ('Animais Peçonhentos', 'Animais Peçonhentos'), ('Arco Voltaico','Arco Voltaico'), ('Atropelamento','Atropelamento'), ('Ruído','Ruído'), ('Choque','Choque')]
    riscos = forms.MultipleChoiceField(choices=risk, widget=forms.CheckboxSelectMultiple(), label='Quais riscos foram detectados?')

    eqp = [('Capacete','Capacete'), ('Manga Isolante','Manga Isolante'), ('Botina Dielétrica', 'Botina Dielétrica'), ('Luva de Cobertura','Luva de Cobertura'), ('Óculos de Proteção','Óculos de Proteção'), ('Protetor Auricular','Protetor Auricular'), ('Luva de Borracha Isolante','Luva de Borracha Isolante'), ('Cinto de Segurança','Cinto de Segurança')]
    equipamentos = forms.MultipleChoiceField(choices=eqp, widget=forms.CheckboxSelectMultiple(), label='Quais equipamentos de segurança serão utilizados?')

    desligamento = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Este serviço requer desligamento ou bloqueio de equipamento ou rede?')

    silz = [('Cone','Cone'),('Giroflex','Giroflex'),('Fita para Isolamento da área','Fita para Isolamento da área'), ('Sinaleira Sonora','Sinaleira Sonora'), ('Cavaletes','Cavaletes'), ('Nenhum','Nenhum')]
    sinalizacao = forms.MultipleChoiceField(choices=silz, widget=forms.CheckboxSelectMultiple(), label='Este serviço requer sinalização?')

    delimitar_area = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Necessita delimitar a área de trabalho?')
    auxconces = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Necessita de auxílio de concessionária local?')
    tensao = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Necessário fazer verificação de tensão?')
    aterramento = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='A inspeção requer aterramento temporário?')
    altura = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='A inspeção será realizada em altura?')
    cinto_seg = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Será necessário se aprisionar à escada e utilização de cinto de segurança?')
    requi_seg = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Os requisitos de segurança foram atendidos por todos?')
    reavaliacao = forms.ChoiceField(choices=simounao, widget=forms.RadioSelect, label='Houve necessidade de reavaliação das inspeções realizadas?')

    class Meta:
        model = models.Relatorio
        fields = ['qualiprof','riscos', 'equipamentos', 'sinalizacao', 'desligamento', 'integridade', 'dialogo', 'curso_nr', 'conferido', 'delimitar_area', 'auxconces', 'tensao', 'aterramento', 'altura', 'cinto_seg', 'requi_seg', 'reavaliacao']

# Avaliação das influencias externas da Instalação elétrica.
class FormRelatorioExternas(forms.ModelForm):
    #exemplo de especificação de field:
    tempambiente = forms.ChoiceField(choices=[('AA1 - Frigorífico (-60 ° a 5 °C)', 'AA1 - Frigorífico (-60 ° a 5 °C)'),('AA2 - Muito frio (-40 ° a 5 °C)','AA2 - Muito frio (-40 ° a 5 °C)'), ('AA3 - Frio (-25 ° a 5 °C)','AA3 - Frio (-25 ° a 5 °C)'), ('AA4 - Temperado (-5 ° a 40 °C)','AA4 - Temperado (-5 ° a 40 °C)'), ('AA5 - Quente (5 ° a 40 °C)','AA5 - Quente (5 ° a 40 °C)'), ('AA6 - Muito quente (5 ° a 60 °C)','AA6 - Muito quente (5 ° a 60 °C)'), ('AA7 - Extrema (-25 ° a 55 °C)','AA7 - Extrema (-25 ° a 55 °C)'), ('AA8 - (-50 ° a 40 °C)','AA8 - (-50 ° a 40 °C)') ] ,label='Temperatura Ambiente')
    condambiente = forms.ChoiceField(choices=[('AB1 - Ambientes internos e externos com temperaturas extremamente baixas', 'AB1 - Ambientes internos e externos com temperaturas extremamente baixas'), ('AB2 - Ambientes internos e externos com temperaturas baixas', 'AB2 - Ambientes internos e externos com temperaturas baixas'), ('AB3 - Ambientes internos e externos com temperaturas baixas', 'AB3 - Ambientes internos e externos com temperaturas baixas'), ('AB4 - Locais abrigados sem controle da temperatura e da umidade. Uso de calefação possível', 'AB4 - Locais abrigados sem controle da temperatura e da umidade. Uso de calefação possível'),  ('AB5 - Locais abrigados com temperatura ambiente controlada', 'AB5 - Locais abrigados com temperatura ambiente controlada'), ('AB6 - Ambientes internos e externos com temperaturas extremamente altas, protegidos  contra  baixas  temperaturas  ambientes. Ocorrência de radiação solar e de calor.', 'AB6 - Ambientes internos e externos com temperaturas extremamente altas, protegidos  contra  baixas  temperaturas  ambientes. Ocorrência de radiação solar e de calor.'), ('AB7 - Ambientes internos e abrigados sem controle  da  temperatura  e  da  umidade.  Podem  ter aberturas para o exterior e são sujeitos a radiação solar.', 'AB7 - Ambientes internos e abrigados sem controle  da  temperatura  e  da  umidade.  Podem  ter aberturas para o exterior e são sujeitos a radiação solar.'), ('AB8  -  Ambientes  externos e sem proteção  contra intempéries, sujeitos a altas e baixas temperaturas', 'AB8  -  Ambientes  externos e sem proteção  contra intempéries, sujeitos a altas e baixas temperaturas')], label='Condições climáticas do ambiente')
    altitude = forms.ChoiceField(choices=[('AC1 Baixa ( ≤ 2000 m )','AC1 Baixa ( ≤ 2000 m )'), ('AC2 Alta ( > 2000 m )', 'AC2 Alta ( > 2000 m )')], label='Altitude')
    presagua = forms.ChoiceField(choices=[('AD1 Desprezível', 'AD1 Desprezível'), ('AD2 Gotejamento' , 'AD2 Gotejamento'), ('AD3 Precipitação', 'AD3 Precipitação'), ('AD4 Aspersão', 'AD4 Aspersão')
,('AD5 Jatos', 'AD5 Jatos')
,('AD6 Ondas', 'AD6 Ondas')
,('AD7 Imersão', 'AD7 Imersão') 
,('AD8 Submersão', 'AD8 Submersão')], label='Presença de água')
    pressolidos = forms.ChoiceField(choices=[], label='Presença de corpos sólidos')
    pressubst = forms.ChoiceField(choices=[], label='Presença de substâncias corrosivas ou poluentes')
    solmecanicas = forms.ChoiceField(choices=[], label='Solicitações mecânicas')
    presmofo = forms.ChoiceField(choices=[], label='Presença de flora e mofo')
    presfauna = forms.ChoiceField(choices=[], label='Presença de fauna')
    infleletro = forms.ChoiceField(choices=[], label='Influências  eletromagnéticas, eletrostáticas ou ionizantes')
    radsolar = forms.ChoiceField(choices=[], label='Radiação solar')
    descatm = forms.ChoiceField(choices=[], label='Descargas atmosféricas')
    movdoar = forms.ChoiceField(choices=[], label='Movimentação do ar')
    vento = forms.ChoiceField(choices=[], label='Vento')
    competencia = forms.ChoiceField(choices=[], label='Competência das pessoas')
    reseletr = forms.ChoiceField(choices=[], label='Resistência  elétrica  do  corpo humano no ambiente')
    contpessoas = forms.ChoiceField(choices=[], label='Contato  das  pessoas  com  o potencial da terra')
    condfuga = forms.ChoiceField(choices=[], label='Condições de fuga das pessoas em emergências')
    natmatpr = forms.ChoiceField(choices=[], label='Natureza dos materiais processados ou armazenados')
    natmatcons = forms.ChoiceField(choices=[], label='Qual a natureza dos materiais de construção')
    classestr = forms.ChoiceField(choices=[], label='Qual a classificação da estrutura das edificações')

    class Meta:
        model = models.Relatorio
        fields = ['tempambiente', 'condambiente', 'altitude', 'presagua', 'pressolidos',
        'pressubst', 'solmecanicas', 'presmofo', 'presfauna', 'infleletro', 'radsolar',
        'descatm', 'movdoar', 'vento', 'competencia', 'reseletr', 'contpessoas', 'condfuga',
        'natmatpr', 'natmatcons', 'classestr']

# Avaliação qualitativa da instalação elétrica.
class FormRelatorioQualitativa(forms.ModelForm):
    #exemplo de especificação de field:
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')

    class Meta:
        model = models.Relatorio
        fields = ['data']

# Avaliação quantitativa da Instalação.
class FormRelatorioQuantitativa(forms.ModelForm):
    #exemplo de especificação de field:
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')

    class Meta:
        model = models.Relatorio
        fields = ['data']
