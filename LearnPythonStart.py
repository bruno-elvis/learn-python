# -*- coding: utf-8 -*- (Muda o formato de texto da linguagem para codificação)
print("Olá mundo")
print(5*5)
"""
Comentário de Várias Linhas """ """
"""
# DEFINIÇÕES DE ALGUMAS VARIÁVEIS E LISTAS
a = 5
b = 10
c = "Maior"
ListaT = [1, 5, 10, 13, 22, 55]
ListaN = ["Bruno", "Elvis", "Pereira", "Silva"]

# TRATAMENTO DE LISTAS
print("TRATAMENTO DE LISTAS")

# UTILIZANDO IF
print("UTILIZANDO IF")
if a > b:
    print(c)
else: #também pode ser utilizado o 'elif' cujo objetivo é ser mais uma condição para ser testada antes de continuar a execução, sendo que só irá cair no 'else' se o 'if' e 'elif' forem falsos
    print("Menor")
    print("")

# UTILIZANDO WHILE
print("UTILIZANDO WHILE")
while a > 0:
    print(a)
    a -= 1 #a = a + 1 (outra forma de se escrever a incrementação)

print("")

# FORMATAÇÃO DE OUTPUT's COM WHILE (SAÍDAS)
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

print("")

zz = 0
while zz < 5:
    print(f"zz vale agora: {zz}") #é o mesmo que esta notação: " print("z vale agora: {}".format(zz)) "
    zz = zz + 1

print("")

Saida1 = "Teste S. 001"
Saida2 = "Teste S. 002"
print("Aqui está o valor da variável 'T1': {} e aqui está o valor da variável 'T2': {}".format(Saida1, Saida2))
print("Aqui está o valor da variável 'T1': {T1} e aqui está o valor da variável 'T2': {T2}".format(T1=Saida2, T2=Saida1)) #exemplo¹ utilizando alias com método "format"

print("")

# FOR E CLASSE 'RANGE'
print("FOR E CLASSE 'RANGE'")
for i in ListaN, ListaT: #pode ser passado uma quantidade ilimitada de objetos para percorrer
    print(i)

print("")
print("RANGE DE TAMANHO 15, INICIADO EM 0 E INCREMENTANDO EM 3")
for i in range(0, 15, 3): #range(início da lista, final da lista, incrementador (passo da contagem))
    print(i)

print("")

# PERCORRENDO STRINGS
print("RETORNA O TAMANHO DO ÍNDICE DENTRO DE UM OBJETO (STRING OU LISTA)")
print("Tamanho da String 'c': " + str(len(c))) #retorna o número de índices em um objeto/container/string/lista
                                               #desconsiderando o '0' como sendo o início da lista (inicia em 1-x)
print("Tamanho do Índice da ListaT (Objetos da Lista): " + str(len(ListaT)))

sizeString = len(ListaN)
print("Tamanho da listaN (Quantidade de Objetos): " + str(sizeString))
#também retorna o tamanho de uma string (inclui os 'espaços' na quantidade total dos índices)
print("")

# NAVEGAÇÃO POR ÍNDICES
print("NAVEGAÇÃO POR ÍNDICES")

print("Objeto no índice '1' da listaN: " + ListaN[1]) #no Python a indexação começa em '0'
print("Caractere no índice '2' da string 'c': " + c[2])

varMeuNome = "Bruno Elvis Pereira Silva"
print ("Trexo exibido começando do índice 6 (inclusivo) até o 11 (excludente): " + varMeuNome[6:12]) #exibe o trecho entre índices [X :(à) Y], recebe = (string[índice incial : índice final] e se denomina "slice" este método de pegar uma parte de uma string
                       #sendo que nesta indexação o primeiro índice [X:] é inclusivo (conta com ele) e o segundo índice [:Y] é excludente (não considera ele na exibição)
print("")
print("Formatação em Caixa-Alta do Objeto no índice '0' da ListaN: " + ListaN[0].upper()) #formatação em caixa alta
print("Formatação em Caixa-Baixa do Objeto no índice '2' da ListaN: " + ListaN[2].lower()) #formatação em minúsculas

print("")

# FUNÇÕES PARA TRATAMENTO DE STRINGS
print("TRABALHANDO COM TRATAMENTO DE STRINGS (FUNÇÕES)")
print("-------------------------------------------------------------------------------------------------")

print("Função 'strip' - varMeuNome: " + varMeuNome.strip()) #remove caracteres especiais ou espaços iniciais e finais de uma string
print("Função 'split' - varMeuNome: ")
print(varMeuNome.split(" ")) #separa o conteúdo de uma string em partes, passando um delimitador como parâmetro / é Case Sensitive
print("")
print("Buscar índice do primeiro caractere da string informada no parâmetro (função 'find'): " + str(varMeuNome.find("Silva"))) #(retorna o índice(posição) do primeiro caractere do parâmetro passado para a busca) / busca um caracter ou conjunto de caracteres dentro de uma string (considerando espaços), é Case-sensitive, caso não encontre o parâmetro definido retorna "-1" e não pode ser chamado em listas
busca = varMeuNome.find("Elvis")
print("Função 'find' passando como parâmetro a variável com o valor de busca: "+ varMeuNome[busca:]) #exibe o texto iniciado numa posição (var = busca) e finalizado em outra posição (sem parámetro de fim = null)
print("")
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
print("")

# DEFINIÇÂO DE FUNÇÕES
print("TRABALHANDO COM FUNÇÕES")

def somar(a, b):
    result = a + b
    print(str(a) + " mais " + str(b) + " é igual a " + str(result))
    return result

def mult(a, b):
    return str(a) + " vezes " + str(b) + " = " + str(a * b)

print("Chamando a função 'somar' passando dois inteiros (5, 10): " + str(somar(5, 10)))
print("Chamando a função 'mult' passando dois inteiros (5, 5): " + mult(5, 5))

print("")

print("RETORNO DE FUNÇÕES ESTATICAMENTE TIPADAS")
def soma (a: int, b: float) -> str: #função com parâmetros tipados (estaticamente tipados)
    return str(a + b) #retorna a soma dos valores numéricos em string definido o tipo do retorno na própria função artravés da parametrização "->"

print("Chamando a função 'soma' passando dois valores tipados (5, 5.5)" + " = " + soma(5, 5.5))

print("")

# MANIPULAÇÃO DE ARQUIVOS #
print("TRABALHANDO COM MANIPULAÇÃO DE ARQUIVOS")
"""
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
"""
insArquivo = open('CONTAS.TXT', 'rt')
#print(insArquivo.read()) #função para ler o arquivo completo no seu formato atual (numa única string)


#linhas = insArquivo.readline() #função para ler e retornar uma linha do arquivo a cada iteração (inicia na linha 1 do arquivo)
#linhas = insArquivo.readlines() #função para ler e retornar todas as linhas do arquivo (retorna uma lista)
#print(linhas)

insArquivo.close() #fecha o arquivo (encerra a instância do objeto manipulador de arquivos)

#newFile = open('TESTE_X.TXT', 'w') #cria um novo arquivo (parâmentro 'w' para modo de escrita)

#Para editar o arquivo:
#newFile.write("Teste de edicao de arquivo")
print("")

# TRABALHANDO COM DICIONÁRIOS
print("TRABALHANDO COM DICIONÁRIOS")
print("")

meuDic = {1: "Valor 1", 2: "Valor 2", 3: "Valor 3", "Quarto": "Valor 4"}

print("meuDic: " + str(meuDic)) #exibe todo o conteúdo do dicionário
print("")
print("Valor de um índice especificado parametricamente: " + meuDic['Quarto']) #exibe valor de um índice especificado pela chave via parâmetro

print("")

print("CONTEÚDO DO DICIONÁRIO (RETORNA SOMENTE AS CHAVES)")
for chave in meuDic: #retorna somente as chaves do dicionário
    print(chave)

print("")

print("VALORES DO DICIONÁRIO (RETORNA EM TUPLAS)")
for i in meuDic.items(): #percorrendo o dicinário (o método "items() retorna as tuplas com as chaves e valores do dicionário")
    print(i)

print("")

print("CHAVES DO DICIONÁRIO (RETORNA AS CHAVES ESPECIFICAMENTE)")
for i in meuDic.keys(): #retorna as chaves de um dicionário através da função "keys()"
    print(i)

print("")

print("VALORES DO DICIONÁRIO (RETORNA OS VALORES)")
for i in meuDic.values(): #retornando os valores do dicionário através do método "values()"
    print(i)

print("")

print("CHAVES E VALORES DO DICIONÁRIO CONCATENADOS")
for chave in meuDic: #exibindo chave + valor concatenados
    print(str(chave) + " - " + meuDic[chave])

print("")

# CLASSE 'RANDOM'
print("TRABALHANDO CLASSE 'RANDOM'")

import random
from typing import cast

num = random.randint(1, 15) #método para gerar um número aleatório com parâmetro inicial e final
print("Número aleatório gerado pelo método 'randint' da classe 'random' (de 1 a 15): " + "(" + str(num) + ")")
print("")

mynums = [1, 10, 5, 25, 15, 13, 55]
num = random.choice(mynums) #o método 'choice' da classe random escolhe um item de uma lista de itens
print("Número escolhido pela função 'choice' na lista 'mynums': " + str(num))
print("")

# TRATAMENTO DE EXCEÇÕES
print("TRABALAHNDO COM EXCEÇÕES")

try:
    print(5 / 0)
except:
    print("Um número não pode ser dividido por 0")
else:
    pass
finally:
    print("10 / 2 = " + str(10 / 2))

# RECEBENDO VALORES PELO MÉTODO 'INPUT'
print("RECEBENDO VALORES PELO MÉTODO 'INPUT'")
print("")
meu_texto = input("Digite um texto: ") #recebendo textos
numero_inteiro = int(input("Digite um numero inteiro: "))#recebendo números
numero_decimal = float(input("Digite um numero decimal: "))#recebendo números
print(meu_texto + " - " + str(numero_inteiro) + " - " + str(numero_decimal))
print("")
print("")

# TRABALHANDO COM SET'S (CONJUNTOS)
print("TRABALHANDO COM SET'S (CONJUNTOS)")
print("")
"""
Conjuntos não possuem noção de ordem por isso seus elementos não podem ser acessados com colchetes [] nem podem ser fatiados.
Os conjuntos (set) não aceitam valores repetidos ao tentar criar um conjunto com valores repetidos eles serão descartados só sobrando um valor do mesmo.
Aceita tipos diferentes como valor (inteiro, flutuante, tupla, string, etc.), mas mão aceita conjuntos mutáveis (listas ou dicionários) como valor.
 """

listaSet = {'Maçã', 'Laranja', 'Uva', 'Abacaxi', 'Maçã', 'Abacate', 'Laranja'} #definindo uma variável do tipo 'set' (um conunto)
setTratado = set(listaSet)
print(setTratado, str(type(listaSet)))

print("Percorrendo o Set tratado pela classe 'set': ")
for sseett in setTratado:
    print(sseett)
print("")

print("Percorrendo o set declarado: ")
for s in listaSet:
    print(s)
print("")

# MOSTRANDO O TIPO DE UM OBJETO
tipObjA = type(a)
tipObjC = type(c)
tipObjT = type((1, 2, 3))
tipObjN = type(ListaN)
tipObjD = type(meuDic)
tipObjS = type(listaSet)

print("Tipo 'Inteiro': " + str(tipObjA))
print("Tipo 'String': "+ str(tipObjC))
print("Tipo 'Tupla': " + str(tipObjT))
print("Tipo 'Lista': " + str(tipObjN))
print("Tipo 'Dicionário': " + str(tipObjD))
print("Tipo 'Conjunto-Set': " + str(tipObjS))