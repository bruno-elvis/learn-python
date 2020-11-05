import numpy as np # Importando a Biblioteca NumPy

fArray = [5, 1, 10, 55, 2]
npArray = np.array(fArray)
fMatriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
npMatriz = np.array(fMatriz)

print()
print("MATRIZ (ARRAY MULTIDIMENSIONAL) COMUM: \n", str(fMatriz), str(type(fMatriz)))
print("")
print("MATRIZ (ARRAY MULTIDIMENSIONAL) NUMPY: \n", str(npMatriz), str(type(npMatriz)))
print("")
print("ARRAY CONVENCIONAL: ", str(fArray), str(type(fArray)))
print("")
print("ARRAY NUMPY: ", str(npArray), str(type(npArray)))
print("")

listaGerada = np.arange(0, 16, 3)
print("LISTA GERADA DE 0 A 16, COM PASSO DE 3:", listaGerada)
print()

print("ARRAY POPULADA COM UMA DETERMINADA QUANTIDADE DE 'ZEROS':", np.zeros(3))
print("ARRAY POPULADA COM UMA DETERMINADA QUANTIDADE DE 'UNS':", np.ones(3))
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'ZEROS':\n", np.zeros((5, 5)))
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'UNS':\n", np.ones((5, 5)))
print()
# MATRIZ IDENTIDADE
print("MATRIZ 'IDENTIDADE' (POPULADA COM 'ZEROS' E 'UNS' UNIFORMEMENTE NA VERTICAL): \n", np.eye(5))
print()

print("POPULAÇÃO DE ARRAY NUMPY IGUALMENTE SEPARADO ENTRE UM ÍNDICE DO ARRAY E OUTRO:", np.linspace(0, 10, 4))#parâmetros principais: ínicio do array, final do array e "passo" do array (espaço igualmente separado entre um índice do array e outro)
print()

# MÉTODO RANDOM
print("-> MÉTODO RANDOM <-")
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
print()
print()
# INDEXAÇÃO EM NUMPY ARRAYS
indArray = np.arange(0, 56, 10)
print(indArray)
print()
#buscado índices dentro de um array numpy
print(indArray[5])
print(indArray[2:5])

# ESTUDAR ANÁLISE EXPORÁTÓRIA #