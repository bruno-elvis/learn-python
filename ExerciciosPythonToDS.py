# PRINTANDO UM ÍNDICE ESPECÍFICO
lst = [1,2,[3,4],[5,[100,200,['Olá']],23,11],1,7]

locLST = lst[3][1][2][0]

print(locLST)
print("")

# PRINTANDO UM ÍNDICE ESPECÍFICO +
dic = {'k1':[1,2,3,{'café':['banana','mulher','colher',{'alvo':[1,2,3,'olá']}]}]}

locDIC = ""
print("")

# EXTRAINDO DOMÍNIO DE UM EMAIL EM UMA STRING
email = "brunoelvis@outlook.com.br"

def obterDominio(email):
    return email.split('@')[-1] #'-1' para capturar o índice de trás para frente ('-1' é sempre o último índice de uma lista)

dominioEmail = obterDominio(email)

print(dominioEmail)
print("")

# BUSCANDO POR UM TERMO EM UMA STRING
string = 'Eu Amo Meu Cachorro Sr. Beethoven!'

def encontreCachorro(st):
    if 'cachorro' in st:
        return 'Au, Au!'
    #elif 'cachorro' in st.lower().split():
        #print('Au')
        #return 'Au!'
    else:
        print('Cachorro não encontrado.')
    
resultadoBusca = encontreCachorro(string)

if resultadoBusca == None:
    resultadoBusca = 'Ops!'
else:
    print("- Beethoven: " + resultadoBusca)

print(resultadoBusca)
print("")

# FILTRANDO PALAVRAS DENTRO DE UMA LISTA
lista = ['sopa','cachorro','salada','gato','ótimo']

busca = list(filter(lambda word: word[0]=='s', lista))

print(busca)
print("")

## ## ## ## ##
def capturarVelocidade(velocidade, aniversario):
    if aniversario:
        velocidade = velocidade - 5
    else:
        velocidade = velocidade

    if velocidade > 80:
        return 'Multa Gravíssima'
    elif velocidade > 60:
            return 'Multa Grave'
    else:
        return 'Não Aplicável'

print(capturarVelocidade(65, True))
print("")

## ## ## ## ##