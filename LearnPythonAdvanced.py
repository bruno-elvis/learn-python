# CONCEITOS AVANÇADOS DE PYTHON #
# Trabalhando com List Comprehension #
listaA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lsitaB = [i*2 for i in listaA] #a listaB recebe o cálculo da raiz quadrada de cada item da listaA
ListaC = [i for i in listaA if i % 2 == 1] #a listaC recebe uma lista com todos os números primos da listaA

print(str(listaA) + " (Lista A)")
print(str(lsitaB) + " (Raiz Quadrada dos Nº's da Lista A)")
print(str(ListaC) + " (Nº's Primos da Lista A)")
print("")

# TRABALHANDO COM A CLASSE 'ENUMERATE' (Obter o Índice de Todos os Elementos)
print("TRABALHANDO COM A CLASSE 'ENUMERATE'")

listaM = ["Yamaha", "BMW", "Kawasaki", "KTM", "Harley-Davidson","Susuki", "Dafra", "Honda"]
print("ENUMERATE MANUAL, UTILIZANDO MODO SIMPLES (GAMBIARRA, MENOS PERFORMÁTICA)")
for i in range(len(listaM)): #primeiro modo
    print(i, listaM[i])

print("")

#segundo modo utilizando enumerate
print("UTILIZANDO A CLASSE ENUMERATE (MANEIRA CERTA DE FAZER ENUMERAÇÕES, MAIS PERFORMÁTICA)")
for indice, fabricante in enumerate(listaM):
    print(indice, fabricante.upper())

print("")
print("LISTA DE FABRICANTES EM ORDEM ALFABÉTICA")
print(sorted(listaM)) #o método 'SORTED' orgazina em ordem (numérica, ou alfabética) uma lista

print("")

# TRABALANDO COM A CLASSE 'MAP'
print("TRABALANDO COM A CLASSE 'MAP'")
def triplo(num): #função para calcular o triplo de um número
    return num * 3

#função 'map' recebe no primeiro parâmetro uma função, que irá ser aplicada a todos os elementos de uma lista, definida no segundo parâmetro
#aoCubo = map(triplo, listaA) #pode-se atribuir o retorno da função 'map' a uma variável
#ou
for numsTriplos in map(triplo, listaA): #pode-se percorrer a lista e exibir os valores de cada índice diretamente no for
    print(numsTriplos)
#ou
listaAoCubo = list(map(triplo, listaA)) #atribuir a uma lista os valores manipulados (ao cubo, neste caso) a uma nova lista
print(listaAoCubo)

print("")

# TRABALHANDO COM A CLASSE 'REDUCE'
print("TRABALHANDO COM A CLASSE 'REDUCE'")
# A função 'reduce' recebe como parâmetro, uma função que será aplicada a uma lista em si (toda ela), sendo o segundo parâmentro a ser passado
from functools import reduce #importanto a classe para uso da função reduce

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

def mult(a, b):
    return (a * b)

print("Total da Multiplicação dos valores informados: " + str(mult(num1, num2)))

print("Multiplicação de todos os valores contidos na listaA: " + str(reduce(mult, listaA)))

print("")

# TRABALHANDO COM A CLASSE 'ZIP' (Junção de duas ou mais listas)
print("TRABALHANDO COM A CLASSE 'ZIP'")

listaN = [28999522013, 221, 15556825700, 28999225731, 28998854427]

listaZIP = zip(listaM, listaN) #une duas listas (lsitaM e listaN) ou mais para ser percorrida

for moto, numero in listaZIP: #percorrendo a lista zipada
    print (moto, numero)

print(list(listaZIP)) #exibindo a lista zipada sem tratamento

# USO DO BREAK, CONTINUE E PASS EM ESTRUTURAS DE REPETIÇÃO

#break: é quebrar, quebra (ou interrompe) o fluxo natural do programa
#continue: é continuar, ou seja, continua o fluxo natural do ciclo
#pass: é passar, ou seja, deixa passar.