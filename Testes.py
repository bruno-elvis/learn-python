i = 0

while i < 5:
    print(f"i vale agora: {i}") #é o mesmo que esta notação: print("i vale agora: {}".format(i))
    i += 1 #ou i = i + 1

print("")
print("")

a = 0

while a < 10:
    print("a agora vale: {}".format(a))
    a = a + 1

print("")
print("")

listaABC = ["A", "B", "C", "D", "E"]
tuplaABC = ("A", "B", "C", "D")
dicABC = {1: "A", 2: "B", 3: "C"}

print("Tamanho do objeto 'listaABC': " + str(len(listaABC)) + " - Tipo: " + str(type(listaABC)))
print("")
print("Tamanho do objeto 'tuplaABC': " + str(len(listaABC)) + " - Tipo: " + str(type(tuplaABC)))
print("")
print("Tamanho do objeto 'dicABC': " + str(len(dicABC)) + " - Tipo: " + str(type(dicABC)))
print("")

print("")
listaProcess = []
listaTest = ["one", "two", "tree", "four"]
for i in listaTest:
    listaProcess.append("five")

print(listaProcess)
print("")
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

apr = 'Aprovado'
rep = 'Reprovado'
resultado = ''
nota = 10

if nota == 10:
    resultado = apr
    print("IF")
elif nota > 5:
    resultado = apr
    print("ELIF")
else:
    resultado = rep
print("Usando ELIF: " + resultado)
print("ELSE")

print("")

if (nota == 5) or (nota > 5):
    resultado = apr
    print("IF")
else:
    resultado = rep
print("Usando ELSE: " + resultado)
print("ELSE")

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
print()

listTrat = ["Aprendendo", "Python"]
listTrat.append("Teste") #adiciona um item no final da lista
print(listTrat)

removeLast = listTrat.pop() #retorna o ultimo valor e remove o mesmo da lista
print(removeLast)
print(listTrat)

removeFirst = listTrat.pop(0) #pode receber como parâmentro o índice do item da lista que será removido
print(removeFirst)
print(listTrat)

# 'IN' = 'Está contido'
listSystem = ['I', 'E', 'A', 'I', 'A', 'I', 'O']
contemA = 'H' in listSystem
contemB = 'A' in listSystem
#é case sensitive
print("A lista {} contém o algarismo 'H'? ->".format(listSystem) + str(contemA))
print("A lista {} contém o algarismo 'A'? -> ".format(listSystem) + str(contemB))

# CLASSE MAP e FILTER
print()

def aoQuadrado (var):
    return var**2

listMapeFil = [9, 5, 1, 9, 1, 9, 15]
print()

mapeando = map(aoQuadrado, listMapeFil) #retorna um objeto do tipo map que deve ser convertido em uma lista por exemplo
mapeandoComLambda = map(lambda x : x**2, listMapeFil)
print(list(mapeando))
print(list(mapeandoComLambda))
print()

filtrandoNumerosImpares = filter(lambda b : b % 2 == 1, listMapeFil) #filtrando números ímpares dentro da lista 'listMapeFil', o método filter deve receber como parâmetros uma função e em seguida um conjunto de dados (lists), e como um terceiro parâmetro pode receber um iterável
print(list(filtrandoNumerosImpares))
print()

print(len(listSystem))
frase = "Minha comida preferida é lasanha."
corteDaFrase = frase.split(" ")
print(frase)
print(len(frase)) #tamanho da string frase (em numero de letras (índices))
print(corteDaFrase)
print(len(corteDaFrase)) #tamanho da lista criada a partir da separação de palavras do método 'split'