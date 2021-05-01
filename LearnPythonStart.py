# -*- coding: utf-8 -*- (Muda o formato de texto da linguagem para codificação)
print("Olá mundo")
print(5*5)
"""
Comentário de Várias Linhas (Criação de Sumários) """ """
"""
# DEFINIÇÕES DE ALGUMAS VARIÁVEIS E LISTAS #
a = 5
b = 10
c = "Maior"
ListaT = [1, 5, 10, 13, 22, 55]
ListaN = ["Bruno", "Elvis", "Pereira", "Silva"]

# TRATAMENTO DE LISTAS #
print("TRATAMENTO DE LISTAS")

# UTILIZANDO IF #
print("UTILIZANDO IF")
if a > b:
    print(c)
else: #também pode ser utilizado o 'elif' cujo objetivo é ser mais uma condição para ser testada antes de continuar a execução, sendo que só irá cair no 'else' se o 'if' e 'elif' forem falsos
    print("Menor")
    print()

# UTILIZANDO WHILE #
print("UTILIZANDO WHILE")
while a > 0:
    print(a)
    a -= 1 #a = a + 1 (outra forma de se escrever a incrementação)

print()

# FORMATAÇÃO DE OUTPUT's COM WHILE (SAÍDAS) #
print("FORMATAÇÃO DE OUTPUT's COM WHILE (SAÍDAS)")
ii = 0
xx = 0
while (ii < 5) and (xx < 5):
    print(f"ii neste índice vale: {ii}") #é o mesmo que esta notação: print("i vale agora: {}".format(i)), '{}' recebe as variáveis que serão substituídas pelo valor das mesmas na string de saída
    print("xx neste índice vale: {}".format(xx))
    print("valor de ii: {} e xx: {}".format(ii, xx)) #outra forma de chamar os outputs a partir de variáveis ou objetos
                                                     #quem define a ordem de saída (output) das informações é o método "format" e não as "{}", exceto quando se utiliza "alias" dentro das "{}" (exemplo¹ abaixo)
    ii = ii + 1
    xx += + 1

print()

zz = 0
while zz < 5:
    print(f"zz vale agora: {zz}") #é o mesmo que esta notação: " print("z vale agora: {}".format(zz)) "
    zz = zz + 1

print()

Saida1 = "Teste S. 001"
Saida2 = "Teste S. 002"
print("Aqui está o valor da variável 'T1': {} e aqui está o valor da variável 'T2': {}".format(Saida1, Saida2))
print("Aqui está o valor da variável 'T1': {T1} e aqui está o valor da variável 'T2': {T2}".format(T1=Saida2, T2=Saida1)) #exemplo¹ utilizando alias com método "format"

print()

# FOR E CLASSE 'RANGE' #
print("FOR E CLASSE 'RANGE'")
for i in ListaN, ListaT: #pode ser passado uma quantidade ilimitada de objetos para percorrer
    print(i)

print()
print("RANGE DE TAMANHO 15, INICIADO EM 0 E INCREMENTANDO EM 3")
for i in range(0, 15, 3): #range(início da lista, final da lista, incrementador (passo da contagem))
    print(i)

print()

# PERCORRENDO STRINGS #
print("RETORNA O TAMANHO DO ÍNDICE DENTRO DE UM OBJETO (STRING OU LISTA)")
print("Tamanho da String 'c': " + str(len(c))) #retorna o número de índices em um objeto/container/string/lista
                                               #desconsiderando o '0' como sendo o início da lista (inicia em 1-x)
print("Tamanho do Índice da ListaT (Objetos da Lista): " + str(len(ListaT)))

sizeString = len(ListaN)
print("Tamanho da listaN (Quantidade de Objetos): " + str(sizeString))
#também retorna o tamanho de uma string (inclui os 'espaços' na quantidade total dos índices)
print()

# NAVEGAÇÃO POR ÍNDICES DE LISTAS #
print("NAVEGAÇÃO POR ÍNDICES")

print("Objeto no índice '1' da listaN: " + ListaN[1]) #no Python a indexação começa em '0'
print("Caractere no índice '2' da string 'c': " + c[2])

varMeuNome = "Bruno Elvis Pereira Silva"
print ("Trexo exibido começando do índice 6 (inclusivo) até o 11 (excludente): " + varMeuNome[6:12]) #exibe o trecho entre índices [X :(à) Y], recebe = (string[índice incial : índice final] e se denomina "slice" este método de pegar uma parte de uma string
                       #sendo que nesta indexação o primeiro índice [X:] é inclusivo (conta com ele) e o segundo índice [:Y] é excludente (não considera ele na exibição)
print()
print("Formatação em Caixa-Alta do Objeto no índice '0' da ListaN: " + ListaN[0].upper()) #formatação em caixa alta
print("Formatação em Caixa-Baixa do Objeto no índice '2' da ListaN: " + ListaN[2].lower()) #formatação em minúsculas

print()

# FUNÇÕES PARA TRATAMENTO DE STRINGS #
print("TRABALHANDO COM TRATAMENTO DE STRINGS (FUNÇÕES)")
print("-------------------------------------------------------------------------------------------------")

print("Função 'strip' - varMeuNome: " + varMeuNome.strip()) #remove caracteres especiais ou espaços iniciais e finais de uma string
print("Função 'split' - varMeuNome: ")
print(varMeuNome.split(" ")) #separa o conteúdo de uma string em partes, passando um delimitador como parâmetro / é Case Sensitive
print()
print("Buscar índice do primeiro caractere da string informada no parâmetro (função 'find'): " + str(varMeuNome.find("Silva"))) #(retorna o índice(posição) do primeiro caractere do parâmetro passado para a busca) / busca um caracter ou conjunto de caracteres dentro de uma string (considerando espaços), é Case-sensitive, caso não encontre o parâmetro definido retorna "-1" e não pode ser chamado em listas
busca = varMeuNome.find("Elvis")
print("Função 'find' passando como parâmetro a variável com o valor de busca: "+ varMeuNome[busca:]) #exibe o texto iniciado numa posição (var = busca) e finalizado em outra posição (sem parámetro de fim = null)
print()
print(varMeuNome.replace("Pereira", "Winchester")) #substitui um trecho ou caractere de uma string, o primeiro parâmetro do método é a busca na string e o segundo é o conjunto de caracteres a bustituir
print("Função 'replace' substititui um valor por outro dentro de uma string: " + varMeuNome)

print("------------------------------------------------------------------------------------------------")

# Conversão (Explícita) de tipos de variáveis
print("CONVERÇÕES EXPLÍCITAS")
print("--------------------------------")

varTXT = "Bruno"
varNUM = 5
varTUP = ("Bruno", "Elvis", "Pereira", "Silva")
#int(varTXT) #valores de texto para número
NUMtoSTR = str(varNUM) #valores de número para texto
TUPtoLST = list(varTUP) #convertendo conjunto de dados para listas
tipoNUMtoSTR = type(NUMtoSTR)
tipoTUPtoLST = type(TUPtoLST)
print(varTXT)
print(varNUM)
print(varTUP)
print()
print(tipoTUPtoLST)
print(tipoNUMtoSTR)

print("--------------------------------")
print()

# DEFINIÇÂO DE FUNÇÕES #
print("TRABALHANDO COM FUNÇÕES")

def somar(a, b):
    result = a + b
    print(str(a) + " mais " + str(b) + " é igual a " + str(result))
    return result

def mult(a, b):
    return str(a) + " vezes " + str(b) + " = " + str(a * b)

print("Chamando a função 'somar' passando dois inteiros (5, 10): " + str(somar(5, 10)))
print("Chamando a função 'mult' passando dois inteiros (5, 5): " + mult(5, 5))

print()

print("RETORNO DE FUNÇÕES ESTATICAMENTE TIPADAS")
def soma (a: int, b: float) -> str: #função com parâmetros tipados (estaticamente tipados)
    return str(a + b) #retorna a soma dos valores numéricos em string definido o tipo do retorno na própria função artravés da parametrização "->"

print("Chamando a função 'soma' passando dois valores tipados (5, 5.5)" + " = " + soma(5, 5.5))

print()

# MANIPULAÇÃO DE ARQUIVOS #
print("TRABALHANDO COM MANIPULAÇÃO DE ARQUIVOS")
'''
# MODOS DE ACESSO (LEITURA E ESCRITA DE ARQUIVOS) DO PARÂMETRO DO MÉTODO 'open()' #
'r'  -> Somente leitura do arquivo;
'w'  -> Escrita (caso o arquivo já exista, será apagado e um novo arquivo vazio será criado);
'a'  -> Leitura e escrita (adiciona o novo conteúdo no final do conteúdo do arquivo);
'b'  -> Modo binário;
'+'  -> Atualização (leitura/escrita);
'r+' -> Leitura e escrita de um arquivo;
'W+' -> Escrita (este modo, assim como o 'w', também apaga o conteúdo anterior do arquivo);
'a+' -> Leitura e escrita (abre o arquivo para atualização);
'x'  -> Abre o arquivo para criação exclusiva, falhando se o arquivo já existir.

# Exemplo de definição:
'open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)'
Ref.: https://docs.python.org/pt-br/3/library/functions.html?highlight=open#open
'''
#insArquivo = open(file='CONTAS.TXT', mode='rt')
#print(insArquivo.read()) #função para ler o arquivo complero no seu formato atual

#linhas = insArquivo.read() #função para ler as linhas do arquivo
#print(linhas)
#print(type(linhas))

#insArquivo.close() #fecha o arquivo (encerra a instância do objeto manipulador de arquivos)

#newFile = open('TESTE_X.TXT', 'w') #cria um novo arquivo (parâmentro 'w' para modo de escrita)

#Para editar o arquivo:
#newFile.write("Teste de edicao de arquivo") #adiciona conteúdo no arquivo ao final
print()

# TRABALHANDO COM DICIONÁRIOS #
print("TRABALHANDO COM DICIONÁRIOS")
print()

meuDic = {1: "Valor 1", 2: "Valor 2", 3: "Valor 3", 'Quarto': "Valor 4"}

print("meuDic: " + str(meuDic)) #exibe todo o conteúdo do dicionário
print()
print("Exibindo tamanho do dicionário 'meuDic' com a função 'len()', retorno: " + str(len(meuDic)) + " (índices).") #Retorna o tamanho do dicionário com a função 'len()'
print()
del meuDic[1] #Exclui um índice de um dicionário através de uma chave, também pode receber a notação 'del(meuDic[1])'
print("Removendo um índice do dicionário atribuído pela chave '1', através da função 'del', retorno: " + str(meuDic))
print()
print("Valores de um índices especificados parametricamente: " + meuDic['Quarto'] + " / " + meuDic[2]) #exibe valor de um índice especificado pela chave via parâmetro
print()
print(2 in meuDic) #verifica se uma chave existe dentro de um dicionário
print(1 not in meuDic) ##verifica se uma chave não existe dentro de um dicionário
print()

print("UTILIZANDO MÉTODO GET(): ")
print("Capturando valor de uma chave válida no dicionário com get(), retorno: " + meuDic.get(3, 'OK')) #Retorna o valor para key se estiver contida no dicionário, caso contrário retorna o valor 'default'.
print("Capturando valor de uma chave inválida no dicionário com get(), retorno 'default': " + meuDic.get(4, 'OK'))
'''
Retorna o valor para key se estiver contida no dicionário, caso contrário retorna o valor 'default'.
Se o valor (parâmetro) 'default' não for definido, retorna por padrão o valor 'None', de tal forma que este método nunca dispara um 'KeyError'.
'''
print()
'''
'setdefault(key, default)'
Se key está no dicionário, retorna o seu valor. Se não, insere key com o valor 'default' e retorna 'default'.
'default' por padrão usa o valor 'None'.
'''
print("Inserindo um novo valor no dicionário caso ele não exista, com a função 'setdefault()', retorno: " + meuDic.setdefault(5, 'Valor 5'))
#Retorna o valor atual da chave passada por parãmetro na função setdefault(chave, valorDefault), caso a chave exista no dicionário
print("Valor do dicionário 'meuDic' atual: " + str(meuDic))
print()

print()

print("CONTEÚDO DO DICIONÁRIO (RETORNA SOMENTE AS CHAVES)")
for i in meuDic: #retorna somente as chaves do dicionário
    print(i)

print()

print("VALORES DO DICIONÁRIO (RETORNA EM TUPLAS)")
for itens in meuDic.items(): #percorrendo o dicinário (o método "items() retorna as tuplas com as chaves e valores do dicionário")
    print(itens)

print()

print("CHAVES DO DICIONÁRIO (RETORNA AS CHAVES ESPECIFICAMENTE (Implementado concatenação com os valores))")
for chaves in meuDic.keys(): #retorna as chaves de um dicionário através da função "keys()"
    print(chaves)

print()

print("VALORES DO DICIONÁRIO (RETORNA OS VALORES)")
for valores in meuDic.values(): #retornando os valores do dicionário através do método "values()"
    print(valores)

print()

print("CHAVES E VALORES DO DICIONÁRIO CONCATENADOS")
for chave in meuDic: #exibindo chave + valor concatenados
    print(str(chave) + " = " + meuDic[chave])

print()

# CLASSE 'RANDOM' #
print("TRABALHANDO CLASSE 'RANDOM'")

import random as rd
from typing import FrozenSet, Union
#from typing import KeysView, cast

num = rd.randint(1, 15) #método para gerar um número aleatório com parâmetro inicial e final
print("Número aleatório gerado pelo método 'randint' da classe 'random' (de 1 a 15): " + "(" + str(num) + ")")
print()

mynums = [1, 10, 5, 25, 15, 13, 55]
num = rd.choice(mynums) #o método 'choice' da classe random escolhe um item de uma lista de itens


print("Número escolhido pela função 'choice' na lista de inteiros 'mynums': " + str(num))
print("Número escolhido pela função 'choice' na lista de strings 'ListaN': " + str(rd.choice(ListaN)))
print()

# TRATAMENTO DE EXCEÇÕES #
print("TRABALAHNDO COM EXCEÇÕES")

try:
    print(5 / 0)
except:
    print("Um número não pode ser dividido por 0")
else:
    pass
finally:
    print("10 / 2 = " + str(10 / 2))

# RECEBENDO VALORES PELO MÉTODO 'INPUT' #
'''
print("RECEBENDO VALORES PELO MÉTODO 'INPUT'")
print()
meu_texto = input("Digite um texto: ") #recebendo textos
numero_inteiro = int(input("Digite um numero inteiro: ")) #recebendo inteiros
numero_decimal = float(input("Digite um numero decimal: ")) #recebendo decimais
print("Imputs concatenados: " + meu_texto + " | " + str(numero_inteiro) + " | " + str(numero_decimal))
print()
'''
print()

# TRABALHANDO COM SET'S (CONJUNTOS) #
print("TRABALHANDO COM SET'S (CONJUNTOS)")
print()
'''
Conjuntos não possuem noção de ordem por isso seus elementos não podem ser acessados com colchetes [] nem podem ser fatiados.
Os conjuntos (set) não aceitam valores repetidos ao tentar criar um conjunto com valores repetidos eles serão descartados só sobrando um valor do mesmo.
Aceita tipos diferentes como valor (inteiro, flutuante, tupla, string, etc.), mas mão aceita conjuntos mutáveis (listas ou dicionários) como valor.
'''
listaS = ['Maçã', 'Laranja', 'Uva', 'Abacaxi', 'Maçã', 'Abacate', 'Laranja'] #declaração de uma lista [] (utiliza-se colchetes)
meuSet = {5, 1.0, "Sete", (1, 2, 3)} #declaração de um set {} (ultiliza-se chaves)
lstSet = set(listaS) #declarando um 'set' através de uma lista

print("Exibindo a lista declarada: " + str(listaS) + " | " + str(type(listaS)))
print("Exibindo o conjunto (set) 'lstSet' a partir da lista 'listaS': " + str(lstSet) + " | " + str(type(lstSet)))
print("Exibindo o conjunto (set) 'meuSet': " + str(meuSet) + ' | ' + str(type(meuSet)))
print()

print("Percorrendo a lista 'listaS' declarada: ")
for lst in listaS:
    print(lst)
print()

print("Percorrendo o set 'lstSet' declarado a partir da lista 'listaS': ")
for s in lstSet:
    print(s)
print()

#declarando um conjunto (set) vazio da forma correta
setVazio = {} #forma errada
print("SET vazio declarado com chaves ({}) retorna (valor): " + str(setVazio) + " | tipo: " + str(type(setVazio)))

setVazio = set() #forma correta
print("SET vazio declarado e instanciado a partir da classe 'set()' retorna (valor): " + str(setVazio) + " | tipo: " + str(type(setVazio)))
print()

'''
Os conjuntos são mutáveis. No entanto, como eles são desordenados, a indexação não tem sentido.
Não podemos acessar ou alterar um elemento de um conjunto usando indexação ou fatiamento.
Podemos adicionar um único elemento, ou vários, utilizando o método 'add', podendo ser tuplas, listas, strings ou outros conjuntos como argumento. Em todos os casos, as duplicatas são evitadas pelo compilador.
Exemplos:
'''
#adicionando e atualizando itens do conjunto (set)
setVazio.add("Bruno")
setVazio.add(5)
setVazio.update([5, 13, 5, "Elvis"]) #notação simples: (set |= other | ...)
print("'setVazio' alterado (add, update): " + str(setVazio))
print()

#removendo itens do conjunto (set)
setVazio.remove("Bruno")
print("Removido valor (Bruno) do 'setVazio': " + str(setVazio))
print("OK")
#setVazio.remove("Bruno")
#print("OK")

setVazio.discard(5)
print("Removido valor (5) do 'setVazio': " + str(setVazio))
print("OK")
setVazio.discard(5)
print("OK")
print()
print("Removendo último índice com a função 'pop()' retorno: " + str(setVazio.pop()))
print("Resultado: " + str(setVazio))

print()
'''
A diferença entre as duas funções é que a função 'remove()' retorna um erro ao tentar remover algum item no conjunto que não existe no mesmo,
já no uso da função 'discard()' não é retornado o erro em questão.
'''

setVazio.clear()
print("'setVazio' limpo, utilizando a função 'clear()' retorno (valor): " + str(setVazio))
print()

# MÉTODOS/FUNÇÕES, OPERAÇÕES LÓGICAS E MATEMÁTICAS PARA TRATAMENTO DE SET'S #
conjA = {0, 1, 2, 5, 10, 13, 15, 25 , 55, 1010, 100}
conjB = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100}

#UNIÃO/JUNÇÃO (SEM VALORES REPETIDOS) DE SETS COM A FUNÇÃO 'union()'
print("UNIÃO/JUNÇÃO (SEM VALORES REPETIDOS) DE SETS COM A FUNÇÃO (union()")
print(conjA | conjB) #notação básica
print(conjA.union(conjB)) #notação orientada a objetos
print()

#INTERSEÇÃO DE SETS COM A FUNÇÃO 'intersection()' (SEM VALORES REPETIDOS)
print("INTERSEÇÃO DE SETS COM A FUNÇÃO 'intersection()' (SEM VALORES REPETIDOS)")
print(conjA & conjB) #notação básica
print(conjA.intersection(conjB)) #notação orientada a objetos
print()

#SET DIFFERENCE
print("SET DIFFERENCE")
print(conjA - conjB) #notação básica
print(conjA.difference(conjB)) #notação orientada a objetos
print(conjB - conjA)
print(conjB.difference(conjA))
print()
print("SET SYMMETRIC DIFFERENCE: ")
print(conjB ^ conjA) #notação básica
print(conjA.symmetric_difference(conjB)) #notação orientada a objetos
print()
print("Verificando se o valor '13' existe no conjunto 'A', retorno: " + str(13 in conjA))
print("Verificando se o valor '13' existe no conjunto 'B', retorno: " + str(13 in conjB))
print("Verificando se o valor '0' não existe no conjunto 'A', retorno: " + str(0 not in conjA))
print("Verificando se o valor '0' não existe no conjunto 'B', retorno: " + str(0 not in conjB))
print("Verificando se o Valor 'Sete' existe no conjunto 'meuSet', retorno: " + str('Sete' in meuSet)) #é case-sensitive na operação de busca
print()
for conteudo in meuSet: #percorrendo um conjunto (set) com FOR
    print(conteudo)
print()

# FUNÇÕES DA CLASSE 'SET' #



# FROZENSET'S (CONJUNTOS (SET'S IMUTÁVEIS)) #
'''
Os SET's são mútaveis e alteraveis não podendo ser utilizado como índices ou chaves.
Já os FROZENSET's são hasháveis ​​e podem ser usados ​​como chaves para um dicionário por exemplo.
'''
fzsBrum = frozenset(['Bruna', 'Bruno'])
print("Definindo uma FROZENSET, retornando seu valor e tipo: " + str(fzsBrum) + " | " + str(type(fzsBrum)))
ba = set('Bruna')
bo = set('Bruno')
nt = set('Nietzsche')
print(ba, bo)
print()

print("Verificando se um conjunto (SET) não possui elementos em comum através da função 'isdisjoint()', retorno: " + str(bo.isdisjoint(nt))) #Retorna 'True' se os conjuntos não tem elementos em comum.
print()
#Conjuntos são disjuntos se e somente se a sua interseção é o conjunto vazio.
'''
issubset(other)
set <= other
Testa se cada elemento do conjunto está contido em other.

set < other
Testa se o conjunto é um subconjunto próprio de other, isto é, set <= other and set != other.

issuperset(other)
set >= other
Testa se cada elemento em other está contido no conjunto.

set > other
Testa se o conjunto é um superconjunto próprio de other, isto é, set >= other and set != other.
'''
print("Retorna uma cópia simples de um conjunto através da função 'copy()', retorno: " + str(bo.copy())) #retorna uma cópia simples de um conjunto
print()
#Atualiza o conjunto, removendo elementos encontrados em outros (set -= other | ...):
print("Atualiza um conjunto removendo os elementos diferente entre os mesmos, através da função 'difference_update()', retorno: " + str(ba.difference_update(nt)))
print()
#Atualiza o conjunto, mantendo somente elementos encontrados em qualquer conjunto, mas não em ambos (set ^= other):
print("Atualiza um conjunto com os elementos contidos em todos os conjuntos, através da função 'symmetric_difference_update()', retorno: " + str(bo.symmetric_difference_update(nt)))
'''
Tembém existe a função 'intersection_update(*others)';
Notação simples (set &= other & ...);
Atualiza o conjunto, mantendo somente elementos encontrados nele e em outros.
'''
print()

# RETORNANDO O TIPOS DE OBJETOS #
tipObjA = type(a)
tipObjC = type(c)
tipObjT = type((1, 2, 3))
tipObjN = type(ListaN)
tipObjD = type(meuDic)
tipObjS = type(lstSet)

print("Tipo 'Inteiro': " + str(tipObjA))
print("Tipo 'String': "+ str(tipObjC))
print("Tipo 'Tupla': " + str(tipObjT))
print("Tipo 'Lista': " + str(tipObjN))
print("Tipo 'Dicionário': " + str(tipObjD))
print("Tipo 'Conjunto-Set': " + str(tipObjS))