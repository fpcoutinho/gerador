from email.policy import default
from django import forms
from . import models
from django.forms.widgets import DateTimeInput, RadioSelect, CheckboxSelectMultiple


# Cria e Edita o relatório inicial, apenas com dados simples.
class FormRelatorioInicial(forms.ModelForm):
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')
    clima = forms.CharField(label='Condições Climáticas:')
    temperatura = forms.IntegerField(label='Temperatura (em °C):')
    responsaveis = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Insira os nomes separados por vírgula (,)'}), label='Responsáveis')

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
    presagua = forms.ChoiceField(choices=[('AD1 Desprezível', 'AD1 Desprezível'), ('AD2 Gotejamento' , 'AD2 Gotejamento'), ('AD3 Precipitação', 'AD3 Precipitação'), ('AD4 Aspersão', 'AD4 Aspersão'),('AD5 Jatos', 'AD5 Jatos'), ('AD6 Ondas', 'AD6 Ondas'), ('AD7 Imersão', 'AD7 Imersão') ,('AD8 Submersão', 'AD8 Submersão')], label='Presença de água')
    pressolidos = forms.ChoiceField(choices=[('AE1 Desprezível', 'AE1 Desprezível'), ('AE2 Pequenos objetos', 'AE2 Pequenos objetos'), ('AE3 Objetos muito pequenos', 'AE3 Objetos muito pequenos'), ('AE4 Poeira leve', 'AE4 Poeira leve'), ('AE5 Poeira moderada', 'AE5 Poeira moderada'), ('AE6 Poeira intensa', 'AE6 Poeira intensa')], label='Presença de corpos sólidos')
    pressubst = forms.ChoiceField(choices=[('AF1 Desprezível', 'AF1 Desprezível'), ('AF2 Atmosférica', 'AF2 Atmosférica'), ('AF3 Intermitente ou acidental', 'AF3 Intermitente ou acidental'), ('AF4 Permanente', 'AF4 Permanente') ], label='Presença de substâncias corrosivas ou poluentes')
    solmecanicas = forms.ChoiceField(choices=[('AG1 Impactos fracos', 'AG1 Impactos fracos'), ('AG2 Impactos médios', 'AG2 Impactos médios'), ('AG3 Impactos severos', 'AG3 Impactos severos'), ('AH1 Vibrações fracas', 'AH1 Vibrações fracas'), ('AH2 Vibrações médias', 'AH2 Vibrações médias'), ('AH3 Vibrações severas', 'AH3 Vibrações severas')], label='Solicitações mecânicas')
    presmofo = forms.ChoiceField(choices=[('AK1 Desprezível', 'AK1 Desprezível'),('AK2 Prejudicial','AK2 Prejudicial')], label='Presença de flora e mofo')
    presfauna = forms.ChoiceField(choices=[('AL1 Desprezível', 'AK1 Desprezível'),('AL2 Prejudicial','AK2 Prejudicial')], label='Presença de fauna')
    infleletro = forms.ChoiceField(choices=[('AM1-1 Harmônicas e inter-harmonicas nível controlado', 'AM1-1 Harmônicas e inter-harmonicas nível controlado'), ('AM1-2 Harmônicas e inter-harmonicas nível normal', 'AM1-2 Harmônicas e inter-harmonicas nível normal'), ('AM1-3 Harmônicas e inter-harmonicas nível alto', 'AM1-3 Harmônicas e inter-harmonicas nível alto'), ('AM2-1 Tensões de sinalização nível controlado', 'AM2-1 Tensões de sinalização nível controlado'), ('AM2-2 Tensões de sinalização nível normal', 'AM2-2 Tensões de sinalização nível normal'), ('AM2-3 Tensões de sinalização nível alto', 'AM2-3 Tensões de sinalização nível alto'), ('AM3-1 Variação de amplitude da tensão nível controlado', 'AM3-1 Variação de amplitude da tensão nível controlado'), ('AM3-2 Variação de amplitude da tensão nível controlado', 'AM3-2 Variação de amplitude da tensão nível controlado'), ('AM4 Desequilíbrio de tensão', 'AM4 Desequilíbrio de tensão'), ('AM5 Variações de frequência', 'AM5 Variações de frequência'), ('AM6 Tensões induzidas de baixa frequência', 'AM6 Tensões induzidas de baixa frequência'), ('AM7 Componentes contínuas em redes C.A.', 'AM7 Componentes contínuas em redes C.A.'), ('AM8-1 Campos magnéticos radiados nível médio (linhas de energia, transformadores, equipamentos de frequência industrial e suas harmônicas)', 'AM8-1 Campos magnéticos radiados nível médio (linhas de energia, transformadores, equipamentos de frequência industrial e suas harmônicas)'), ('AM8-2 Campos magnéticos radiados nível alto (grande proximidade dos itens mencionados em AM8-1)', 'AM8-2 Campos magnéticos radiados nível alto (grande proximidade dos itens mencionados em AM8-1)'), ('AM9-1 Campo elétrico nível desprezível', 'AM9-1 Campo elétrico nível desprezível'), ('AM9-2 Campo elétrico nível médio', 'AM9-2 Campo elétrico nível médio'), ('AM9-3 Campo elétrico nível alto', 'AM9-3 Campo elétrico nível alto'), ('AM9-4 Campo elétrico nível muito alto', 'AM9-4 Campo elétrico nível muito alto'), ('AM21 perturbações de modo comum geradas por campos eletromagnéticos modulados em AM ou FM', 'AM21 perturbações de modo comum geradas por campos eletromagnéticos modulados em AM ou FM'), ('AM22-1 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível desprezível', 'AM22-1 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível desprezível'), ('AM22-2 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível médio', 'AM22-2 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível médio'), ('AM22-3 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível alto', 'AM22-3 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível alto'), ('AM22-4 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível muito alto', 'AM22-4 Transitórios unidirecionais conduzidos na faixa do nanossegundo nível muito alto'), ('AM23-1 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível controlado', 'AM23-1 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível controlado'), ('AM23-2 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível médio', 'AM23-2 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível médio'), ('AM23-3 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível alto', 'AM23-3 Transitórios unidirecionais conduzidos na faixa do micro ao milissegundo nível alto'), ('AM24-1 Transitórios oscilantes conduzidos nível médio', 'AM24-1 Transitórios oscilantes conduzidos nível médio'), ('AM24-2 Transitórios oscilantes conduzidos nível alto', 'AM24-2 Transitórios oscilantes conduzidos nível alto'), ('AM25-1 Fenômenos radiados de alta frequência nível desprezível', 'AM25-1 Fenômenos radiados de alta frequência nível desprezível'), ('AM25-2 Fenômenos radiados de alta frequência nível médio', 'AM25-2 Fenômenos radiados de alta frequência nível médio'), ('AM25-3 Fenômenos radiados de alta frequência nível alto', 'AM25-3 Fenômenos radiados de alta frequência nível alto'), ('AM31-1 Descargas eletrostáticas nível baixo', 'AM31-1 Descargas eletrostáticas nível baixo'), ('AM31-2 Descargas eletrostáticas nível médio', 'AM31-2 Descargas eletrostáticas nível médio'), ('AM31-3 Descargas eletrostáticas nível alto', 'AM31-3 Descargas eletrostáticas nível alto'), ('AM31-4 Descargas eletrostáticas nível muito alto', 'AM31-4 Descargas eletrostáticas nível muito alto'), ('AM41-1 Radiações ionizantes perigosas', 'AM41-1 Radiações ionizantes perigosas')], label='Influências  eletromagnéticas, eletrostáticas ou ionizantes')
    radsolar = forms.ChoiceField(choices=[('AN1 Desprezível', 'AN1 Desprezível'), ('AN2 Média', 'AN2 Média'), ('AN3 Alta', 'AN3 Alta')], label='Radiação solar')
    descatm = forms.ChoiceField(choices=[('AQ1 Desprezíveis', 'AQ1 Desprezíveis'),('AQ2 Indiretas', 'AQ2 Indiretas'),('AQ3 Diretas', 'AQ3 Diretas')], label='Descargas atmosféricas')
    movdoar = forms.ChoiceField(choices=[('AR1 Desprezível', 'AR1 Desprezível'), ('AR2 Média', 'AR2 Média'), ('AR3 Forte','AR3 Forte')], label='Movimentação do ar')
    vento = forms.ChoiceField(choices=[('AS1 Desprezível', 'AS1 Desprezível'), ('AS2 Médio', 'AS2 Médio'), ('AS3 Forte','AS3 Forte') ], label='Vento')
    competencia = forms.ChoiceField(choices=[('BA1 Comuns','BA1 Comuns'),('BA2 Crianças', 'BA2 Crianças'),('BA3 Incapacitadas','BA3 Incapacitadas'), ('BA4 Advertidas', 'BA4 Advertidas'), ('BA5 Qualificadas', 'BA5 Qualificadas')], label='Competência das pessoas')
    reseletr = forms.ChoiceField(choices=[('BB1 Alta', 'BB1 Alta'), ('BB2 Normal', 'BB2 Normal'), ('BB3 Baixa', 'BB3 Baixa'), ('BB4 Muito baixa', 'BB4 Muito baixa')], label='Resistência  elétrica  do  corpo humano no ambiente')
    contpessoas = forms.ChoiceField(choices=[('BC1 Nulo', 'BC1 Nulo'), ('BC2 Raro', 'BC2 Raro'), ('BC3 Frequente', 'BC3 Frequente'), ('BC4 Contínuo', 'BC4 Contínuo')], label='Contato  das  pessoas  com  o potencial da terra')
    condfuga = forms.ChoiceField(choices=[('BD1 Normal', 'BD1 Normal'), ('BD2 Longa', 'BD2 Longa'), ('BD3 Tumultuada', 'BD3 Tumultuada'), ('BD4 Longa e tumultuada', 'BD4 Longa e tumultuada')], label='Condições de fuga das pessoas em emergências')
    natmatpr = forms.ChoiceField(choices=[('BE1 Riscos desprezíveis', 'BE1 Riscos desprezíveis'), ('BE2 Riscos de incêndio', 'BE2 Riscos de incêndio'), ('BE3 Riscos de explosão', 'BE3 Riscos de explosão'), ('BE4 Riscos de contaminação', 'BE4 Riscos de contaminação')], label='Natureza dos materiais processados ou armazenados')
    natmatcons = forms.ChoiceField(choices=[('CA1 Não combustíveis','CA1 Não combustíveis'),('CA2 Combustíveis','CA2 Combustíveis')], label='Qual a natureza dos materiais de construção')
    classestr = forms.ChoiceField(choices=[('CB1 Riscos desprezíveis', 'CB1 Riscos desprezíveis'), ('CB2 Sujeitas a propagação de incêndio', 'CB2 Sujeitas a propagação de incêndio'), ('CB3 Sujeitas a movimentação', 'CB3 Sujeitas a movimentação'), ('CB4 Flexíveis ou instáveis', 'CB4 Flexíveis ou instáveis')], label='Qual a classificação da estrutura das edificações')

    class Meta:
        model = models.Relatorio
        fields = ['tempambiente', 'condambiente', 'altitude', 'presagua', 'pressolidos',
        'pressubst', 'solmecanicas', 'presmofo', 'presfauna', 'infleletro', 'radsolar',
        'descatm', 'movdoar', 'vento', 'competencia', 'reseletr', 'contpessoas', 'condfuga',
        'natmatpr', 'natmatcons', 'classestr']


# Avaliação qualitativa da instalação elétrica.
class QualiWidget(forms.MultiWidget):
    def __init__(self, *args,**kwargs):

        myChoices = kwargs.pop("choices",[])
        widgets = (
            forms.Select(choices=myChoices),
            forms.Textarea(attrs={'placeholder': 'Observações'}),
        )
        super(QualiWidget, self).__init__(widgets, *args,**kwargs)
    
    def decompress(self, value):
        if isinstance(value, str):
            if(value == ''):
                return ''
            obj, obs = value.split(': ')
            return [obj, obs]

class QualiField(forms.MultiValueField):

    widget = QualiWidget

    def __init__(self, *args,**kwargs):
        myChoices = kwargs.pop("choices")
        fields = (
            forms.ChoiceField(choices=myChoices),
            forms.CharField(required=False),
        )
        super(QualiField,self).__init__(fields,*args,**kwargs)
        self.widget=QualiWidget(choices=myChoices)
    
    def compress(self, value):
        return f'{value[0]}: {value[1]}' if isinstance(value, list) else ''


class FormRelatorioQualitativa(forms.ModelForm):
    
    escolhas = [('Sim', 'Sim'), ('Não', 'Não'), ('Parcialmente', 'Parcialmente')]
    documentacao = QualiField(choices=escolhas, label='Há documentação da instalação e esta inclui plantas, esquemas unifilares e outros, detalhes de montagem, memorial descritivo, especificações de componentes, parâmetros de projeto?')
    ambientesofreu = QualiField(choices=escolhas, label='O ambiente sofreu alguma reforma e a documentação foi atualizada ou acrescida de algum aditivo de projeto?')
    instalacaoinspecionada = QualiField(choices=escolhas, label='A instalação foi inspecionada antes da entrada em funcionamento e existe algum documento atestando esse fato?')
    linhaseletricasdisp = QualiField(choices=escolhas, label='As linhas elétricas estão dispostas de modo a permitir verificações, ensaios, reparos ou modificação da instalação?')
    compinstalacao = QualiField(choices=escolhas, label='Os componentes da instalação foram selecionados e instalados levando-se em conta as influências externas?')
    linhaseletricascorr = QualiField(choices=escolhas, label='As linhas elétricas estão corretamente instaladas?')
    tomadasdeforca = QualiField(choices=escolhas, label='As tomadas de força existentes atendem ao novo padrão nacional NBR 14136/2002?')
    qtdesufitomadas = QualiField(choices=escolhas, label='O ambiente apresenta tomadas de força em quantidade suficiente?')
    instlquadist = QualiField(choices=escolhas, label='O quadro de distribuição está devidamente instalado em local de fácil acesso à manutenção, inspeção e ensaio?')
    novoscircuitos = forms.ChoiceField(choices=[('Nenhuma', 'Nenhuma'), ('Até 6', 'Até 6'), ('7 a 12', '7 a 12'), ('13 a 30', '13 a 30'), ('N > 30', 'N > 30')], label='Há disponibilidade de criação de novos circuitos no quadro de distribuição?')
    advquadist = QualiField(choices=escolhas, label='Há indicações de advertência nos quadros de distribuição?')
    dispprotecaoident = QualiField(choices=escolhas, label='Os dispositivos de proteção estão dispostos e identificados de forma fácil de reconhecer os respectivos circuitos protegidos?')
    protcircuitos = QualiField(choices=escolhas, label='A proteção dos circuitos é compatível com a bitola dos condutores?')
    barramentoquadist = QualiField(choices=escolhas, label='O Quadro de distribuição possui barramento de neutro e aterramento?')
    bitola = QualiField(choices=escolhas, label='Todas as conexões estão com terminais apropriados para cada bitola utilizada?')
    condutident = QualiField(choices=escolhas, label='Os condutores estão identificados por cores ou conforme sua função?')
    disjundif = QualiField(choices=escolhas, label='Existe disjuntor diferencial residual instalado no quadro de distribuição?')
    dispprotecaosurtos = QualiField(choices=escolhas, label='Existe dispositivo de proteção contra surtos de tensões?')
    servseguranca = QualiField(choices=escolhas, label='Há elementos para serviços de segurança a exemplo de iluminação de emergência, exaustores de fumaça, etc?')
    esqaterramento = forms.ChoiceField(choices=[('TN-S', 'TN-S'), ('TN-C-S', 'TN-C-S'), ('TN-C', 'TN-C'), ('TT', 'TT'), ('IT','IT')], label='Qual o esquema de aterramento utilizado?')
    reservadeenergia = QualiField(choices=escolhas, label='Existe fonte alternativa ou de reserva de energia?')
    fontseguranca = QualiField(choices=escolhas, label='Existe fonte de segurança de energia?')
    paralelismo = QualiField(choices=escolhas, label='Há mecanismos para evitar o paralelismo das fontes?')

    class Meta:
        model = models.Relatorio
        fields = ['documentacao', 'ambientesofreu', 'instalacaoinspecionada', 'linhaseletricasdisp', 'compinstalacao', 'linhaseletricascorr', 'tomadasdeforca', 'qtdesufitomadas', 'instlquadist', 'novoscircuitos', 'advquadist', 'dispprotecaoident', 'protcircuitos', 'barramentoquadist', 'bitola', 'condutident', 'disjundif', 'dispprotecaosurtos', 'servseguranca', 'esqaterramento', 'reservadeenergia', 'fontseguranca', 'paralelismo']


# Avaliação quantitativa da Instalação.
class FormRelatorioQuantitativa(forms.ModelForm):
    #exemplo de especificação de field:
    data = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}),input_formats='%d/%m/%Y %H:%M', label='Data e Hora da inspeção:')

    class Meta:
        model = models.Relatorio
        fields = ['data']
