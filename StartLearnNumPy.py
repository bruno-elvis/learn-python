<<<<<<< HEAD
import numpy as np
#from numpy.core.fromnumeric import amax # Importando a Biblioteca NumPy

fArray = [5, 1, 10, 55, 2] #declaração lista/array
npArray = np.array(fArray)
fMatriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] #declaração de uma matriz do tipo 'list'
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
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'ZEROS':\n", np.zeros((5, 5))) # 'zeros(colunas, linhas)'
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'UNS':\n", np.ones((5, 5))) # 'ones(colunas, linhas)'
print()
# MATRIZ IDENTIDADE
print("MATRIZ 'IDENTIDADE' (POPULADA COM 'ZEROS' E 'UNS' UNIFORMEMENTE NA VERTICAL): \n", np.eye(5))
print()
#
print("POPULAÇÃO DE ARRAY NUMPY IGUALMENTE SEPARADO ENTRE UM ÍNDICE DO ARRAY E OUTRO:", np.linspace(0, 10, 4)) #parâmetros principais: ínicio do array, final do array e "passo" do array (espaço igualmente separado entre um índice do array e outro)
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
print("RETORNANDO O ÍNDICE EM QUE SE ENCONTRA O INTEIRO MÁXIMO  DENTRO DE UM ARRAY-NP (arrayDeInteiros):", str(arrayDeInteiros.argmax()))
print("RETORNANDO O ÍNDICE EM QUE SE ENCONTRA O INTEIRO MÍNIMO DENTRO DE UM ARRAY-NP (arrayDeInteiros):", str(arrayDeInteiros.argmin()))
print()
print()

# INDEXAÇÃO EM NUMPY ARRAYS
indArray = np.arange(0, 56, 10)
print(indArray)
print()

#BUSCANDO ÍNDICES DENTRO DE UM ARRAY NUMPY
print("BUSCANDO ÍNDICE NO ARRAY PASSANDO O ÍNDIDE NO PARÂMENTRO (indArray): ", indArray[5]) #parâmetro inclusivo
print("BUSCANDO ÍNDICES NO ARRAY PASSANDO OS ÍNDIDES DO INTERVALO NO PARÂMENTRO (indArray): ", indArray[2:5]) #parâmetros inclusivos
print("RETORNANDO TODOS OS VALORES COM INICIO NO ÍNDICE '0': ", indArray[:3]) #valores do numpy array do índice 0 ao 3
print("RETORNANDO TODOS OS VALORES COM INICIO NO ÍNDICE '2': ", indArray[2:]) #valores do numpy array do índice 2 ao último do array
print()

indArray[1:3] = 55
print("DEFININDO TODOS OS VALORES DE UM INTERVALO DE UM ARRAY POR PARÂMETRO: ", indArray) #defini todos os valores do índice 1 ao 3 para '55'

## PERCORRENDO ARRAY'S MULTIDIMENCIONAIS ##
aMulti = np.arange(50).reshape(5, 10) #criando um array multidimensional com 50 valores de 0 a 49, tratando para ser um array de 10 colunas e 5 linhas

print(aMulti)
print()

tam_aMulti = np.shape(aMulti)
print("Tamanho do array multidimensional (aMulti): ", tam_aMulti)
print()

print(aMulti[:3]) #retornando as primeiras 3 linhas da matriz
print()

'''
* IMPORTANTE *
No Python variáveis com valores recebidos de outros objetos/variáveis REFERENCIAM o próprio objeto, recebem uma referencia do objeto de origem
'''
aMulti2 = aMulti[:3]
aMulti2[:3] = 99

print("Matriz tratada (aMulti2) : \n", aMulti2)
print()
print("Matriz original (aMulti) : \n", aMulti)
print()

'''
* IMPORTANTE *
Neste caso para trabalhar com os valores pertencentes apenas à nova variável definida, pode-se utilizar o método 'copy()'
'''
aMulti2 = aMulti[:3].copy()
aMulti2[:3] = 99

print("Array multidimencional recebendo a cópia dos valores de outro array (não referenciando): \n", aMulti2)
print()
print("Matriz original (aMulti) : \n", np.arange(50).reshape(5, 10)) #= aMulti
print()

# FATIANDO (SLICE) ARRAY MULTIDIMENCIONAIS #
fatiaDoArray = aMulti[3:5, 7] #retornando a coluna de índice 7 (6ª coluna), das linhas de índice 3 à 5 (4ª e 5ª linhas)
print("Retornando a 6ª coluna das 4ª e 5ª linhas na matriz'aMulti': ", fatiaDoArray)
print()

cemArray = np.arange(100) #declarando um array numpy de 100 índices (0 à 99)
print("Tamahno do 'cemArray':", np.shape(cemArray), "- do Tipo:", type(cemArray))
print()

cemMatriz = cemArray.reshape(10, 10) #definindo um array multidimensional numpy com 10 colunas e 10 linhas (tuplas)
# o método 'reshape()' do numpy vai retornar erro caso a multiplicação das colunas, vezes as linhas não for igual ao total de índices do array origem
print("Tamanho do array multidimensional 'cemMatriz':", np.shape(cemMatriz), "- do Tipo:", type(cemMatriz))

quintuplosNoArray = cemArray % 5 == 0 #array que recebe o valor do índice do array origem, se o retorno da condição passada (resto da divisão por 5 for 0) for 'True', para cada índice do array numpy de origem (referência)
quintuplosNaMatriz = cemMatriz % 5 == 0
print()
print("Imprimindo os índices que a condição foi 'True' no array 'quintuplosNoArray': \n", cemArray[quintuplosNoArray])
print()
print("Imprimindo os índices que a condição foi 'True' no array 'quintuplosNaMatriz': \n", cemMatriz[quintuplosNaMatriz])
print()

=======
import numpy as np
#from numpy.core.fromnumeric import amax # Importando a Biblioteca NumPy

fArray = [5, 1, 10, 55, 2] #declaração lista/array
npArray = np.array(fArray)
fMatriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]] #declaração de uma matriz do tipo 'list'
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
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'ZEROS':\n", np.zeros((5, 5))) # 'zeros(colunas, linhas)'
print("MATRIZ POPULADA COM UMA DETERMINADA QUANTIDADE DE 'UNS':\n", np.ones((5, 5))) # 'ones(colunas, linhas)'
print()
# MATRIZ IDENTIDADE
print("MATRIZ 'IDENTIDADE' (POPULADA COM 'ZEROS' E 'UNS' UNIFORMEMENTE NA VERTICAL): \n", np.eye(5))
print()
#
print("POPULAÇÃO DE ARRAY NUMPY IGUALMENTE SEPARADO ENTRE UM ÍNDICE DO ARRAY E OUTRO:", np.linspace(0, 10, 4)) #parâmetros principais: ínicio do array, final do array e "passo" do array (espaço igualmente separado entre um índice do array e outro)
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
print("RETORNANDO O ÍNDICE EM QUE SE ENCONTRA O INTEIRO MÁXIMO  DENTRO DE UM ARRAY-NP (arrayDeInteiros):", str(arrayDeInteiros.argmax()))
print("RETORNANDO O ÍNDICE EM QUE SE ENCONTRA O INTEIRO MÍNIMO DENTRO DE UM ARRAY-NP (arrayDeInteiros):", str(arrayDeInteiros.argmin()))
print()
print()

# INDEXAÇÃO EM NUMPY ARRAYS
indArray = np.arange(0, 56, 10)
print(indArray)
print()

#BUSCANDO ÍNDICES DENTRO DE UM ARRAY NUMPY
print("BUSCANDO ÍNDICE NO ARRAY PASSANDO O ÍNDIDE NO PARÂMENTRO (indArray): ", indArray[5]) #parâmetro inclusivo
print("BUSCANDO ÍNDICES NO ARRAY PASSANDO OS ÍNDIDES DO INTERVALO NO PARÂMENTRO (indArray): ", indArray[2:5]) #parâmetros inclusivos
print("RETORNANDO TODOS OS VALORES COM INICIO NO ÍNDICE '0': ", indArray[:3]) #valores do numpy array do índice 0 ao 3
print("RETORNANDO TODOS OS VALORES COM INICIO NO ÍNDICE '2': ", indArray[2:]) #valores do numpy array do índice 2 ao último do array
print()

indArray[1:3] = 55
print("DEFININDO TODOS OS VALORES DE UM INTERVALO DE UM ARRAY POR PARÂMETRO: ", indArray) #defini todos os valores do índice 1 ao 3 para '55'

## PERCORRENDO ARRAY'S MULTIDIMENCIONAIS ##
aMulti = np.arange(50).reshape(5, 10) #criando um array multidimensional com 50 valores de 0 a 49, tratando para ser um array de 10 colunas e 5 linhas

print(aMulti)
print()

tam_aMulti = np.shape(aMulti)
print("Tamanho do array multidimensional (aMulti): ", tam_aMulti)
print()

print(aMulti[:3]) #retornando as primeiras 3 linhas da matriz
print()

'''
* IMPORTANTE *
No Python variáveis com valores recebidos de outros objetos/variáveis REFERENCIAM o próprio objeto, recebem uma referencia do objeto de origem
'''
aMulti2 = aMulti[:3]
aMulti2[:3] = 99

print("Matriz tratada (aMulti2) : \n", aMulti2)
print()
print("Matriz original (aMulti) : \n", aMulti)
print()

'''
* IMPORTANTE *
Neste caso para trabalhar com os valores pertencentes apenas à nova variável definida, pode-se utilizar o método 'copy()'
'''
aMulti2 = aMulti[:3].copy()
aMulti2[:3] = 99

print("Array multidimencional recebendo a cópia dos valores de outro array (não referenciando): \n", aMulti2)
print()
print("Matriz original (aMulti) : \n", np.arange(50).reshape(5, 10)) #= aMulti
print()

# FATIANDO (SLICE) ARRAY MULTIDIMENCIONAIS #
fatiaDoArray = aMulti[3:5, 7] #retornando a coluna de índice 7 (6ª coluna), das linhas de índice 3 à 5 (4ª e 5ª linhas)
print("Retornando a 6ª coluna das 4ª e 5ª linhas na matriz'aMulti': ", fatiaDoArray)
print()

cemArray = np.arange(100) #declarando um array numpy de 100 índices (0 à 99)
print("Tamahno do 'cemArray':", np.shape(cemArray), "- do Tipo:", type(cemArray))
print()

cemMatriz = cemArray.reshape(10, 10) #definindo um array multidimensional numpy com 10 colunas e 10 linhas (tuplas)
# o método 'reshape()' do numpy vai retornar erro caso a multiplicação das colunas, vezes as linhas não for igual ao total de índices do array origem
print("Tamanho do array multidimensional 'cemMatriz':", np.shape(cemMatriz), "- do Tipo:", type(cemMatriz))

quintuplosNoArray = cemArray % 5 == 0 #array que recebe o valor do índice do array origem, se o retorno da condição passada (resto da divisão por 5 for 0) for 'True', para cada índice do array numpy de origem (referência)
quintuplosNaMatriz = cemMatriz % 5 == 0
print()
print("Imprimindo os índices que a condição foi 'True' no array 'quintuplosNoArray': \n", cemArray[quintuplosNoArray])
print()
print("Imprimindo os índices que a condição foi 'True' no array 'quintuplosNaMatriz': \n", cemMatriz[quintuplosNaMatriz])
print()

>>>>>>> c8c6db1f6c461ce06eb5644698db2e8e2d427641
### ESTUDAR ANÁLISE EXPORÁTÓRIA ###