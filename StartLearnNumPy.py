import numpy as np

fArray = [5, 1, 10, 55, 2]
npArray = np.array(fArray)
fMatriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
npMatriz = np.array(fMatriz)

print(str(fMatriz) + str(type(fMatriz)))
print("")
print(str(npMatriz) + str(type(npMatriz)))
print("")
print(str(fArray) + str(type(fArray)))
print("")
print(str(npArray) + str(type(npArray)))
print("")

listaGerada = np.arange(0, 16, 3)
print(listaGerada)

print(np.zeros(3))
print(np.ones(3))
print(np.zeros((5, 5)))
print(np.ones((5, 5)))
print()
# MATRIZ IDENTIDADE
print(np.eye(5))
print()

print(np.linspace(0, 10, 4))#parâmetros principais: ínicio do array, final do array e "passo" do array (espaço igualmente separado entre um indice do array e outro)
print()

# MÉTODO RANDOM
#np.random() -> gerar números aleatórios com diversas regras possíveis
#np.random.rand() -> submétodo do método 'random', gera em um intervalo determinado (parâmetro) de números com igual probabilidade (distribuição uniforme) de serem gerados, entre 0 e 1.
arrayDeInteiros = np.random.randint(0, 50, 3) #um array de 0 a 50 contendo 3 índices (submétodo para gerar números inteiros e aleátórios dentro de um intervalo parametrizado)

print(np.random.rand(5)) # 5 índices de números de 0 a 1 (distribuição uniforme)
print()
print(np.random.rand(5) * 100) # 5 índices de números de 0 a 100
print()
print(np.random.randn(5)) # 5 índices de números de -1 a 1 (Distribuição normal (gaussiana) de média 0 e desvio padrão 1 (mais aplicável na prática))
print()
print(arrayDeInteiros) #um array de 0 a 50 contendo 3 índices (submétodo para gerar números inteiros e aleátórios dentro de um intervalo parametrizado)
print()
print(np.shape(arrayDeInteiros)) #saber o tamanho em (colunas, linhas) de um array do numpy
print()
print("Máximo: " + str(arrayDeInteiros.max()))
print("Mínimo: " + str(arrayDeInteiros.min()))
print("Índice que se encontra o número máximo: " + str(arrayDeInteiros.argmax()))
print("Índice que se encontra o número mínimo: " + str(arrayDeInteiros.argmin()))
