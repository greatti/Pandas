# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 12:30:44 2021

@author: great
"""

'''
agora vamos começar a importar arquivos de dados .csv e interpreta-los, modifica-los etc
'''
import pandas as pd
pd.options.display.max_columns = None #para nao ter limite de colunas
pd.options.display.max_rows = None #para nao ter limite de linhas

df = pd.read_csv('admission.csv')
print(df.head())

'''
primeira coisa que vemos: como nao escolhemos um index, o pandas usou o default começando em 0
mas e se quisermos definir uma das colunas como index? 

o Serial No. é um bom dandidato:
    '''
df = pd.read_csv('admission.csv', index_col = 0) #fazemos com que a coluna de indexes suma
print(df.head())
'''
agora o que foi utilizado como index é a primeira variavel do DataFrame, ou seja, 'o Serial No.' 

podemos ainda modificar esse df renomeando as colunas, mas como? :
    usando rename() criamos um dicionario com (nomes antigos = keys) e (nomes novos = values)
'''
ndf = df.rename(columns = {'GRE Score' : 'GRE Score', 
                              'TOEFL Score' : 'TOEFL Score', 
                              'University Rating' : 'University Rating', 
                              'SOP' : 'Statement of Purpose', 
                              'LOR' : 'Letter of Recommendation', 
                              'CGPA' : 'CGPA', 
                              'Research' : 'Research', 
                              'Chance of Admit' : 'Chance of Admit'})
''' veja que tivemos que
renomear nome por nome das colunas, ate mesmo aqueles que nao queriamos renomear '''
print(ndf.head())
'''
os nomes modificados foram:
    SOP -> Statement of Purpose
    LOR -> Letter of Recommendation
mas veja que LOR nao mudou, enquanto SOP sim, por que? vamos verificar isso usando .columns()
'''
print(ndf.columns)
''' veja:
    LOR não mudou porque o nome real é 'LOR ' com um whitespace, e isso gera problemas
    O mesmo ocorre para 'Chance of Admit ', se tentarmos mudar sem o whitespace nao da certo
podemos então ou adicionar o whitespace quando formos escrever o dicionario de mudança ou 
procurar um outro metodo que ignore os whitespaces


vamos por enquanto apenas aplicar a mudança mais crua, ou seja, usando 'LOR ' : 'Letter of Recommendation'
'''
ndf = ndf.rename(columns = {'LOR ' : 'Letter of Recommendation'})
#veja que nem precisamos escrever todos os nomes novamente, só aquele que queremos mudar
print(ndf.head())
print(ndf.columns)
'''
como visto, isso é MUITO FRAGIL, pois depende de voce verificar os nomes das colunas
existe uma função que LIMPA OS NOMES e depois RENOMEIA
A função de cortar whitespaces se chama strip() 
'''
ndf = ndf.rename(mapper = str.strip, axis = 'columns')
print(ndf.columns, '\n') #e pronto, agora em 'Chance of Admit' não há mais whitespace, compare com df:
print(df.columns) #entao vamos aplicar ao df tb
df = df.rename(mapper = str.strip, axis = 'columns')
print(df.columns)

print(df.head())
df = df.rename(columns = {'LOR' : 'Letter of Recommendation', 
                          'SOP' : 'Statement of Purpose', })
print(df.head(), '\n')
print(df.columns)

''' AGORA SIM ESTA TUDO CERTO '''

'''
vamos praticar agora uma mudança em TODOS os nomes das colunas : 
'''
colunas = list(df.columns) #para criar uma lista com os nomes das colunas do dataframe
print(colunas)

#vamos aplicar uma mudança que faz com que fique tudo minusculo
colunas = [x.lower().strip() for x in colunas] #isso vai deixar tudo minusculo E retirar whitespaces
df.columns = colunas
print(df.head())
print(df.columns)

''' e assim como lower tb podemos fazer upper: '''
colunas = [x.upper().strip() for x in colunas] #isso vai deixar tudo minusculo E retirar whitespaces
df.columns = colunas
print(df.head(), '\n')
print(df.columns)

#===================================================================================================
''' a partir daqui limpa as variaveis '''

import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('admission.csv', index_col = 0) #lembre que index_col = 0 é para remover o index padrao
df.columns = [x.lower().strip() for x in df.columns] #para manter tudo minusculo e sem whitespace
print(df.head())
print(df.columns)
print(df['chance of admit'])
'''
vamos fazer a nossa primeira limpeza de dados:
    supomos que QUEREMOS APENAS AQUELES DADOS CUJO CHANCE OF ADMIT É MAIOR QUE 0.7
'''
#primeiramente devemos criar uma segunda dataframe, vamos chamar de admitmask construida a partir de df para chanceofadmit > 0.7
admit_mask = df['chance of admit'] > 0.7
''' admit_mask será uma matriz booleana que mostrará True ou False para cada Serial No. '''
print(admit_mask.head(10))
''' meio ruim, porque podemos querer uma matriz só dos serial no. que tiverem chance of admit > 0.7 

para fazer isso, aplicamos a condição 'admit_mask' a df, ou seja:
'''
print(df.where(admit_mask).head(10)) #Ou seja, printar df onde a condição da admit_mask se aplica
'''
nesse caso perceba que onde a admit_mask nao se aplica o SerialNo. admite o valor NaN...

se queremos desprezar os NaN ja aprendemos que existe a funçao dropna()
'''
print(df.where(admit_mask).dropna().head(10)) 
''' 
dessa forma observamos apenas os SerialNo que possuem ChanceOfAdmit > 0.7 

tivemos que juntar funções demais para conseguir o nosso objetivo, utilizar where().dropna() é um 
pouco inutil pois existe uma função que faz essas duas funções juntas: 
    '''
print(df[df['chance of admit'] > 0.7].head())
'''
OU SEJA:
    Se escrevemos df[df[]] estamos basicamente omitindo where()dropna()
'''
''' existe tambem a forma de retirar apenas uma das colunas de dentro do dataframe: '''
print(df['gre score'].head()) 
'''mas tambem podemos retirar duas: '''
print(df[['gre score', 'toefl score']].head())
'''e tambem podemos retirar uma dataframe com todos os dados de todos aqueles que
tiveram uma gre_score > 320

veja que isso é muito diferente do feito anteriormente, antes nós obtivemos uma lista
da chance_of_admit apenas daqueles que tivessem > 0.7
dessa vez estamos obtendo uma lista de todos os dados dada essa condição '''
print(df[df['gre score'] > 320].head())



'''
AGORA SABEMOS APLICAR UM CRITERIO DE FILTRO, 
como aplicar varios filtros? 

usando o & podemos fazer isso:
'''
print((df['chance of admit'] > 0.7) & (df['chance of admit'] > 0.9)) 
''' esse print vai retornar uma lista booleana, TRUE para os que obedecerem as duas condições apenas 

podemos melhorar um pouco a cara disso: '''

print((df['chance of admit'].gt(0.7)) & (df['chance of admit'].lt(0.9))) #.gt representa >     .lt representa <
print(df['chance of admit'].gt(0.7).lt(0.9)) #e assim nao precisamos escrever df['chance of admit'] duas vezes

#=====================================================================================================================================================
''' vamos redefinir tudo de novo '''
import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('admission.csv', index_col = 0)
df.columns = [x.lower().strip() for x in df.columns] #para ajeitar o nome das coulunas
print(df.head())
print(df.columns)

''' em algum momento podemos querer, por exemplo, que o index não seja mas Serial No. como ficou definido 
por index_col = 0, as vezes podemos querer que esteja organizado com base em outra informação

vamos colocar como index a 'chance of admit':
'''
df['chance of admit'] = df.index
df = df.set_index('chance of admit')
print(df.head())

''' e se quisermos voltar o index para o default basta utilizar a função
reset_index() '''
df = df.reset_index()
print(df.head())


''' e se quisermos agora criar um multiindex? ou seja, mais de um index

para isso vamos mudar o nosso dataframe '''

df = pd.read_csv('census.csv') #possui 100 colunas
print(df.head())

'''quero ver todos os valores de uma unica coluna na forma de uma lista

ou seja, diferente daquela primeira forma que fizemos'''
print(df['SUMLEV'].unique()) #aqui ganhamos uma lista falando que SÓ EXISTEM DOIS POSSIVEIS VALORES NESSA COLUNA: 40 E 50
print(df['SUMLEV']) #aqui mostra literalmente todos os 3192 elementos variando entre 40 e 50

''' e agora queremos apenas os elementos cujo SUMLEV assume valores 50 '''
df = df[df['SUMLEV'] == 50] #vai nos retornar todos os dados a respeito daqueles cuja SUMLEV == 50
print(df.head())

'''tem muita informação nesse df, é até lerdo de produzir, então vamos reduzir esse df: '''

keepcolumns = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 
                   'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011','POPESTIMATE2012',
                   'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']

df = df[keepcolumns]
print(df.head())

''' e agora vamos finalmente setar um multiindex, STNAME e STYNAME '''
df = df.set_index(['STNAME', 'CTYNAME'])
print(df)
''' por causa disso, veja que primeiramente df está organizado por estados, dentro dos estados estao as
cidades e para cada cidade encontramos as informações 

Claro que ainda está muito dificil encontrar determinada informação de determinada cidade em determinado 
estado, mas vamos facilitar: '''

print(df.loc['Michigan', 'Washtenaw County']) #Viu como é facil?

''' E se quisermos comparar duas cidades de dois estados? '''

print(df.loc[[('Michigan', 'Washtenaw County'),
             ('Michigan', 'Wayne County')]])

#===================================================================================================

import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None
df = pd.read_csv('class_grades.csv')
print(df.head(15))

''' vamos limpar esses dados, ja vimos que existem dados de certos alunos que estao com NaN

vamos usar isnull() que cria uma boolean_mask em todo o dataframe 
'''
mask = df.isnull() #que identifica onde estao os NaN
print(mask) #onde há True é porque existe uma NaN
'''se lembrarmos de dropna() podemos descartar todos os valores que são NaN de df'''
print(df.dropna().head(15))
''' ou tambem podemos preencher todos os NaN com algum dado especifico, -1 por exemplo'''
df.fillna(-1, inplace = True)#assim estamos aplicando uma função a df que modificara para sempre
print(df.head(15))

####################### VAMOS TROCAR DE DOCUMENTO #############################
import pandas as pd
df = pd.read_csv('log.csv')
pd.options.display.max_columns = None
pd.options.display.max_rows = None
print(df.head(15))

''' a titulo de organização vamos setar 'time' como index'''
df = df.set_index(['time'])
print(df.head(15))
''' e tambem podemos organizar o index em ordem crescente de tempo '''
df = df.sort_index()
print(df.head(15))

''' como dois usuarios ou mais podem utilizar o sistema ao mesmo tempo então devemos
fazer uma multiindexação: '''
df = df.reset_index()
df = df.set_index(['time', 'user'])
print(df.head(15))

del df['index']
print(df.head(15))

''' veja como existem muitos NaN, vamos preenche-los com alguma coisa que preste
usando a funçao ffill()

se usarmos ffill aqui, todos os valores de 'paused' serão dados como False, isso porque
os NaN são substituidos verticalmente pelo valor anterior
os de 'volume' sairão todos como 10

se quisermos preencher dessa forma, verticalmente, basta fazermos ffill e usar axis = 0 e
nesse caso não faz sentido usar axis = 1 pois temos que preencher verticalmente mesmo 

ainda podemos usar bfill se quisermos preencher de baixo para cima 
'''
df = df.fillna(method = 'ffill', axis = 0, inplace = False) '''inplace = false para nao substituir '''
print(df.head(15))

''' e podemos substituir alguns valores pelo q quisermos '''
print(df.replace([10,5], ['maximo', 'medio']))
print(df.head(20))

''' vamos detectar, na coluna de video, todos q terminam com .html e substituir por 'webpage' 
qualquer numero de caracteres = .* que terminam em .html = .html$
'''
print(df.replace(to_replace = '.*.html$', value = 'webpage', regex = True))

#===================================================================================================

import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('presidents.csv', index_col = 0)
print(df.head())
print(df.columns)
#vamos deixar tudo sem whitespace no final
df = df.rename(mapper = str.strip, axis = 'columns')
print(df.columns)
print(df.head())
#e agora vamos colocar tudo no minusculo
colunas = list(df.columns) #para criar uma lista com os nomes das colunas do dataframe
print(colunas)

colunas = [x.lower().strip() for x in colunas] #isso vai deixar tudo minusculo E retirar whitespaces
df.columns = colunas
print(df.head())
print(df.columns)

''' a primeira missão será cortar os dados da coluna 'president', queremos separar em PRIMEIRO 
e SEGUNDO nomes:
    
vamos criar uma função chamada splitname()
'''
def splitname(row):
    row['first'] = row['president'].split(' ')[0]
    #a coluna 'first' vai ser a palavra de index 0 do split dos dados da coluna 'president'
    #(' ') indica que o split será feito a cada whitespace, ('.') indicaria que o split seria feito a cada ponto
    row['last'] = row['president'].split(' ')[-1]
    #o mesmo se aplica a 'last', dessa vz pegando o index -1, ou seja, a ultima palavra sempre
    return row

'''vamos aplicar a função agora utilizando apply() '''
df = df.apply(splitname, axis = 'columns') #aplicar a função splitname a df sobre as colunas
print(df.head(), '\n')
print(df.columns)
'''agora temos que deletar a coluna ['president'] '''
del df['president']
print(df.head(), '\n')
print(df.columns)
''' e vamos definir como index ['first'] e ['last'] '''
df = df.set_index(['first', 'last'])
print(df.head())

##################### podemos fazer a mesma coisa usando regexes ############################import pandas as pd
pd.options.display.max_columns = None
pd.options.display.max_rows = None

df = pd.read_csv('presidents.csv', index_col = 0)
#vamos deixar tudo sem whitespace no final
df = df.rename(mapper = str.strip, axis = 'columns')
#e agora vamos colocar tudo no minusculo
colunas = list(df.columns) #para criar uma lista com os nomes das colunas do dataframe
colunas = [x.lower().strip() for x in colunas] #isso vai deixar tudo minusculo E retirar whitespaces
df.columns = colunas
print(df.head())
print(df.columns)

''' primeiro precisamos definir um padrão a ser seguido 

nesse caso, queremos pegar o a primeira palavra e a ultima de 'presidents'
'''
pattern = '(^[\w]*)(?:.* )([\w]*$)' #e assim definimos tres grupos
'''
o primeiro : o começo da string, qualquer caractere ou digito, em qualquer quantidade
o segundo : nao queremos que retorne, qualquer numero de caracteres seguidos por uma whitespace
o terceiro : qualquer numero de caractere mas ligado ao fim da string

vamos colocar nome nos grupos
'''
pattern = '(?P<First>^[\w]*)(?:.* )(?P<Last>[\w]*$)'
names = df['president'].str.extract(pattern).head() 
#aqui estamos dizendo: defina como (names) o nosso PATTERN aplicado a ['president'] 
print(names)

''' mas veja que se printarmos df ainda nao temos First e Last : '''
print(df.head(), '\n')
print(df.columns)
''' entao vamos adicionar essas colunas que criamos a df '''
df['First'] = names['First']
df['Last'] = names['Last']
print(df.head())
''' e agora se quisermos podemos defini-las como indexes tb'''


''' ['BORN'] é uma coluna muito problematica, muito bagunçada, vamos deixa-la mais 'clean'
começando por excluir tudo aquilo que nao segue o padrao de
mes/dia/ano
'''
df['born'] = df['born'].str.extract('([\w]{3} [\w]{1,2}, [\w]{4})')
'''
([\w]{3} [\w]{1,2}) indica quaisquer caracteres de 3 de tamanho seguido por um whitespace seguido por qualquer caractere de tamanho de 1 a 2
seguido por virgula, whitespace e ([\w]{4}) indica quaisquer caracteres de tamanho 4
'''

print(df['born'].head())
'''
se ainda quisermos deixar mais organizado a forma das datas podemos usar .to_datetime:
'''

df['born'] = pd.to_datetime(df['born'])
print(df['born'].head())

print(df.head())

df = df.set_index(['First', 'Last'])
print(df.head(), '\n')
print(df.columns)

'''vamos supor que queremos organizar os presidentes do mais novo pro mais velho 
na idade em que assumiu o cargo '''

df = df.reset_index()
df = df.set_index(['age atstart of presidency'])
df = df.sort_index()
print(df['president'].head(30))
print(df['president'])
''' ou seja o presidente mais novo dos USA assumiu com 42 anos, Theodore , o mais velho com 69, Reagan '''





















