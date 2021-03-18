import numpy as np # Importando a Biblioteca NumPy

fArray = [5, 1, 10, 55, 2]
npArray = np.array(fArray)
fMatriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
npMatriz = np.array(fMatriz)

print()
print("MATRIZ (ARRAY MULTIDIMENSIONAL) COMUM: \n", str(fMatriz), str(type(fMatriz)))
print()
print("MATRIZ (ARRAY MULTIDIMENSIONAL) NUMPY: \n", str(npMatriz), str(type(npMatriz)))
print()
print("ARRAY CONVENCIONAL: ", str(fArray), str(type(fArray)))
print()
print("ARRAY NUMPY: ", str(npArray), str(type(npArray)))
print()

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
#
print("POPULAÇÃO DE ARRAY NUMPY IGUALMENTE SEPARADO ENTRE UM ÍNDICE DO ARRAY E OUTRO:", np.linspace(0, 10, 4))#parâmetros principais: ínicio do array, final do array e "passo" do array (espaço igualmente separado entre um índice do array e outro)
print()

# MÉTODO RANDOM
print("-> MÉTODO RANDOM <-")
#np.random() -> gerar números aleatórios com diversas regras possíveis
#np.random.rand() -> submétodo do método 'random', gera em um intervalo determinado (parâmetro) de números com igual probabilidade (distribuição uniforme) de serem gerados, entre 0 e 1.

arrayDeInteiros = np.random.randint(0, 50, 3) #um array de 0 a 50 contendo 3 índices (submétodo para gerar números inteiros e aleátórios dentro de um intervalo parametrizado)

print("UMA QUANTIDADE DETERMINADA DE ÍNDICES PASSADA POR PARÂMETRO (5) DISTRIBUIDA UNIFORMEMENTE ENTRE 0 E 1:", np.random.rand(5)) # 5 índices de números de 0 a 1 (distribuição uniforme)
print()
print("UMA QUANTIDADE DETERMINADA DE ÍNDICES PASSADA POR PARÂMETRO (5) DISTRIBUIDA UNIFORMEMENTE ENTRE 0 E 100:", np.random.rand(5) * 100) # 5 índices de números de 0 a 100
print()
print("UMA QUANTIDADE DETERMINADA DE ÍNDICES PASSADA POR PARÂMETRO (5) COM DISTRIBUIÇÃO NORMAL DE MÉDIA 0 E DESVIO PADRÃO 1, ENTRE -1 E 1:", np.random.randn(5)) # 5 índices de números de -1 a 1 (Distribuição normal (gaussiana) de média 0 e desvio padrão 1 (mais aplicável na prática))
print()
print("ARRAY COM INTEIROS ALEATÓRIOS DE 0 a 50, CONTENDO 3 ÍNDICES:\n", arrayDeInteiros) #um array de 0 a 50 contendo 3 índices (submétodo para gerar números inteiros e aleátórios dentro de um intervalo parametrizado)
print()
print("RETORNA O TAMANHO EM (COLUNAS, LINHAS) DE UM ARRAY NUMPY (arrayDeInteiros):", np.shape(arrayDeInteiros)) #saber o tamanho em (colunas, linhas) de um array do numpy
print()
print("INTEIRO MÁXIMO DO ARRAY (arrayDeInteiros):", str(arrayDeInteiros.max()))
print("INTEIRO MÍNIMO DO ARRAY (arrayDeInteiros):", str(arrayDeInteiros.min()))
print("ÍNDICE QUE SE ENCONTRA O INTEIRO MÁXIMO (arrayDeInteiros):", str(arrayDeInteiros.argmax()))
print("ÍNDICE QUE SE ENCONTRA O INTEIRO MÍNIMO (arrayDeInteiros):", str(arrayDeInteiros.argmin()))
print()
print()
# INDEXAÇÃO EM NUMPY ARRAYS
indArray = np.arange(0, 56, 10)
print(indArray)
print()
#buscado índices dentro de um array numpy
print("BUSCANDO ÍNDICE NO ARRAY PASSANDO O ÍNDIDE NO PARÂMENTRO (indArray):", indArray[5])
print("BUSCANDO ÍNDICES NO ARRAY PASSANDO OS ÍNDIDES DO INTERVALO NO PARÂMENTRO (indArray):", indArray[2:5])


# ESTUDAR ANÁLISE EXPORÁTÓRIA #