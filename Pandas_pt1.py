# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:03:35 2021

@author: great
"""

import pandas as pd
''' vamos criar a nossa primeira SERIE em PANDAS '''
students = ['Alice', 'James', 'Sally'] #uma LISTA como ja conhecemos
print(students) #para vermos como está a lista
S_students = pd.Series(students) #para criar uma SERIE
print(S_students)
'''
veja que o pandas gerou uma Serie com linhas e colunas, de indexes 0 1 2 porque não especificamos 
o index que queriamos, esse é o padrão 

vamos criar uma serie com numeros ao invés de strings agora
'''
numbers = [1,2,3]
S_numbers = pd.Series(numbers)
print(S_numbers)
'''
PERCEBA:
    dtype da serie com STRINGS = object
    dtype da serie com INTS = int64

o que aconteceria se houvesse um dado faltando na lista?
'''
l3 = [1, 2, None]
Sl3 = pd.Series(l3)
print(Sl3)
'''
agora veja que dtype = float e os numeros da serie foram automaticamente transformados em float
e, alem disso, há um dado chamado NaN que significa NotANumber

não se pode interpretar, no entanto, NaN como um None, pois ele é alguma coisa
'''
import numpy as np
np.NaN == None #esse teste da FALSO
print(type(np.NaN))
print(type(None))

''' existem algumas funções para o NaN que trabalham apenas com o NaN: '''
print(np.isnan(np.nan)) #confirmamos que NaN é NaN
print(np.isnan(1)) #não se confirma que 1 é NaN

'''
vamos lembrar:
    criamos uma SERIE através de uma LISTA
    podemos criar uma SERIE através de um DICIONARIO, os indexes se tornam as keys 
'''
students_scores = {'Alice' : 'Physics', 
                   'Jon' : 'Chem', 
                   'Sally' : 'Math'}
s = pd.Series(students_scores)
print(s) #podemos ver que as keys do dicionario se tornaram os indexes da Serie
print(s.index)  #aqui isso se confirma 

'''
E se criarmos uma SERIE não por uma lista, ou um dicionario, mas por uma LISTA DE TUPLAS? '''
students = [('Alice', 'Brown'), ('Jack', 'White'), ('Molly', 'Green')]
ss = pd.Series(students)
print(ss)
print(ss.index)



''' e se nao quisermos criar nem uma lista nem um dicionario? '''
s = pd.Series(['Physics', 'Chemistry', 'English'], index = [ 'Alice', 'Jack', 'Molly'])
print(s)


''' e se criarmos um dicionario com informação a mais e pedirmos uma serie com informação faltando?'''
dicionario = {'Alice' : 'Physics', 
              'Jack' : 'English', 
              'Molly' : 'Chemistry'}

s = pd.Series(dicionario, index = ['Alice', 'Molly', 'Sam'])
''' veja quem Jack existe no dicionario mas Sam não '''
print(s)
''' Jack é descartado pois nao se pede informação dele mas Sam é colocado como NaN pois há MissingData '''

'''
uma serie da pandas pode ser questionada por sua POSIÇÃO DE INDEX ou por sua ETIQUETA DE INDEX
Se voce NÃO DER um index à serie quando questionada, a POSIÇAO e a ETIQUETA serão dadas como valores iguais

Para questionar com a POSIÇÃO DE INDEX, começando do zero, usar (iloc())
Para questionar com a ETIQUETA DE INDEX, usamos (loc())
'''
students_classes = { 'Alice' : 'Physics',
                    'Jack' : 'Chemistry', 
                    'Molly' : 'English', 
                    'Sam': 'History'}
s = pd.Series(students_classes)
print(s)
'''se quisermos olhar o dado sobre a Sam? então perguntamos pelo INDEX 3 ou pela KEY SAM '''
print(s.iloc[3]) #INDEX
print(s.loc['Sam']) #KEY

'''Se x em s[x] for um INT o python automaticamente interpreta como um index
Se x em s[x] for um STR o python automaticamente interpreta como uma key
isso é problema porque as veze nossas keys são INT
'''
print(s[3]) #apenas um INT sem indicar se é loc ou iloc, vai resultar numa leitura por index
print(s['Molly']) #apenas um STR sem indicar se é loc ou iloc, vai resultar numa leitura por key

'''agora vamos ver o caso que da problema '''
class_code = { 99: 'Physics', 
              100: 'Chemistry', 
              101: 'English', 
              120: 'History'}
s = pd.Series(class_code)
print(s)

print(s[3]) #dará uma Keyerror porque nossas keys são int também, nesse caso temos que especificar
print(s.iloc[3]) #agora sim


''' vamos criar uma serie com dados que representam as notas de um aluno '''
grades = pd.Series([100, 90, 88, 76, 60, 20, 99, 43, 13])
total = np.sum(grades) #sim, podemos somar todos os elementos de uma Serie
media = total/len(grades) #sim, podemos tirar o tamanho total da Serie também
print(media)

######### PODEMOS FAZER DE OUTRO JEITO MAIS 'AUTOMATICO' ############
grades = pd.Series([100, 90, 88, 76, 60, 20, 99, 43, 13])
total = 0
provas = 0
for grade in grades:
    total = grade + total
    provas = provas + 1
print(total/provas)

''' vamos criar uma serie de inteiros '''
s = pd.Series([1, 2, 3])
print(s)
s.loc['History'] = 99 #vamos adicionar um elemento de index HISTORY de valor 99 
print(s)
'''mesmo que seja de TYPE DIFERENTE o Pandas não tem problema em adicionar esse elemento à serie 

mas e se quisermos que o mesmo index tenha varios valores? '''

students_classes = pd.Series({ 'Alice' : 'Physics',
                              'Jack' : 'Chemistry',
                              'Molly' : 'English',
                              'Sam' : 'History'})
print(students_classes)
#E aí vamos adicionar mais elementos criando uma segunda serie:
kelly_classes = pd.Series(['Philosophy', 'Arts', 'Math'], index = ['Kelly', 'Kelly', 'Kelly'])
#E vamos adicionar os elementos dessa serie na serie anterior
all_students_classes = students_classes.append(kelly_classes)
print(all_students_classes)
'''
OBS: As series (kelly_classes) e (students_classes) NÃO foram destruidas, elas foram unidas e 
criou-se uma nova serie independente
'''
print(all_students_classes.loc['Kelly'])

#===================================================================================================

'''
vamos agora trabalhar em juntar varias Series em apenas um frame, chamado DATAFRAME
'''
record1 = pd.Series({'Name' : 'Alice', 
                         'Class' : 'Physics',
                         'Score' : 85})
record2 = pd.Series({'Name' : 'Jack', 
                         'Class' : 'Chemistry',
                         'Score' : 82})
record3 = pd.Series({'Name' : 'Helen', 
                         'Class' : 'Biology', 
                         'Score' : 90})
''' aqui temos informações sobre 3 pessoas, com suas respectivas materias e notas
para juntar as 3 series precisamos chamar uma função chamada DataFrame, geralmente representada por df
'''
df = pd.DataFrame([record1, record2, record3], 
                  index = ['school1', 'school2', 'school3'])
''' veja que adicionamos indexes arbitrarios porque nao queriamos os padroes 0 1 2 '''
print(df) #e agora temos como se fosse uma matriz, com as linhas marcando os indexes e as colunas cada grupo da classe

'''se quisermos, nao precisamos definir x series, podemos definir apenas UMA SERIE contendo todas as infos 
É como se fosse varias series dentro de uma variavel só 
'''
records = [{'Name' : 'Alice', 
                 'Class' : 'Physics',
                 'Score' : 85}, 
            {'Name' : 'Jack', 
                 'Class' : 'Chemistry',
                 'Score' : 82}, 
            {'Name' : 'Helen', 
                 'Class' : 'Biology', 
                 'Score' : 90}] 

df = pd.DataFrame(records, index = ['school1', 'school2', 'school3'])
print(df)
''' e ainda podemos usar iloc e loc '''
print(df.iloc[2], '\n')
print(df.loc['school3'])

'''podemos ser ainda mais especificos e não pegar apenas uma linha, mas combinar uma linha e uma coluna: '''
print(df.loc['school3', 'Name'])
print(df.loc['school3']['Name']) #isso corresponde ao anterior, nao muda nada
print(df.loc['school1', 'Class'])

'''
e se quisermos procurar por colunas, nao por linhas? porque dessa forma só conseguimos encontrar os 
itens de 'school1', 'school2' ou 'school3'.

bom, podemos fazer uma transposta, assim as colunas se tornam linhas e as linhas colunas: '''

dft = df.T
print(dft) #e agora podemos pesquisar
print(dft.loc['Name'])
''' e tambem podemos pesquisar um par'''
print(dft.loc['Name', 'school3']) #o mesmo que ja encontramos na linha 202
print(dft.loc['Class', 'school1']) #o mesmo que ja encontramos na linha 204

'''
Mas isso foi muito dificil, tivemos que transformar df em uma transposta para podemos chamar as colunas? 
nao da pra fazer isso direto?
da sim: 
    '''
print(df['Name'], '\n') #simplesmente, para encontrar colunas
print(df.loc['school1']) #para encontrar linhas

'''
como printar mais de uma coluna? '''

print(df)
print(df.loc[:,['Name', 'Score']]) #nesse caso entamos pegando TODAS AS LINHAS(:), as colunas Name e Score
print(df.loc['school2':, ['Name', 'Score']]) #aqui sao das linhas 1 e 2, as colunas Name e Score

'''
e se quisermos deletar dados de um dataframe? 
aqui devemos usar a função drop() para deletar dados usando apenas um parametro
a função drop não modifica a sua Data.Frame, na verdade ela cria uma copia e modifica a copia

'''
print(df.drop('school1')) #veja que agora temos df mas sem a linha 'school1'
'''no entanto se printarmos df ainda continuamos com ela inteira '''
print(df)
#ele continua intacto
'''drop() entretanto possui outros dois parametros opcionais, 
o primeiro : inplace; se for True o DF vai ser atualizado ao inves de criar uma copia
o segundo : axes; indica o que deve ser dropado, por padrão é zero
'''

dfcopy = df.copy()
print(dfcopy) #vamos fazer uma copia só pra garantir a segurança de df
print(df)

dfcopy.drop('school2')
print(dfcopy) #continua o mesmo
'''mas se fizermos inplace = True '''
dfcopy.drop('school2', inplace=True)
print(dfcopy) #dfcopy foi modificada para sempre

'''vamos fazer uma transposta de df'''
dft = df.T
print(dft)
print(dft.drop('Name')) #aqui vai excluir o axis 'Name' nao permanentemente, que é uma linha 
'''vamos lembrar que em df 'Name' é uma coluna, se quisermos deletar a coluna temos que 
utilizar o parametro axis = 1 para indicar que é uma coluna '''
print(df)
print(df.drop('Name', axis = 1)) #se executarmos a função sem o axis o python vai tentar achar uma linha chamada 'Name' e nao vai achar

'''
mas da pra fazer isso de forma mais simples? deletar uma linha OU uma coluna? sem distinção? 
SIM, usando a função del()
'''
del df['Name']
print(df) #no entanto, dessa forma, o dataframe fica modificado para sempre
'''
da mesma forma tambem conseguimos adicionar informação a um dataframe 
'''
df['ClassRank'] = {1, 3, 2} #ele vai criar uma nova coluna ClassRank e associar as chaves 1, 2 e 3 a school1 school2 e school3
print(df)


#==================================    FIM    =================================















