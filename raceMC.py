from random import Random, randint, random #para importar o random
from time import sleep #para importar a pausa antes do sorteio
from operator import itemgetter, not_
from random import sample

def pontuacao ():
    pontos = randint(1, 13) * 3
    return pontos

corridinha = {"Yamaha":pontuacao(),
              "BMW":pontuacao(),
              "Kawasaki":pontuacao(),
              "KTM":pontuacao(),
              "Harley-Davidson":pontuacao(),
              "Susuki":pontuacao(),
              "Dafra":pontuacao(),
              "Honda":pontuacao()}

print("========== INÍCIO DA CORRIDA ==========")
for motinha, rank in corridinha.items():
    print(f"{motinha} fez {rank} pontos ") #"f" forma abreviada para o método format()
    sleep(2)

ranking = sorted(corridinha.items(), key=itemgetter(1),reverse=True)
print(ranking)

print("-="*50)

print("========== CHEGADA ==========")
for rank, motinha in enumerate(ranking):
    print(f"{rank+1}º lugar: {motinha[0]}")

from random import Random, randint, random #para importar o random
from time import sleep #para importar a pausa antes do sorteio
from operator import itemgetter, not_
from random import sample

def pontuacao ():
    pontos = randint(1, 13) * 3
    return pontos

corridinha = {"Yamaha":pontuacao(),
              "BMW":pontuacao(),
              "Kawasaki":pontuacao(),
              "KTM":pontuacao(),
              "Harley-Davidson":pontuacao(),
              "Susuki":pontuacao(),
              "Dafra":pontuacao(),
              "Honda":pontuacao()}

print("========== INÍCIO DA CORRIDA ==========")
for motinha, rank in corridinha.items():
    print(f"{motinha} fez {rank} pontos ") #"f" forma abreviada para o método format()
    sleep(2)

ranking = sorted(corridinha.items(), key=itemgetter(1),reverse=True)
print(ranking)

print("-="*50)

print("========== CHEGADA ==========")
for rank, motinha in enumerate(ranking):
    print(f"{rank+1}º lugar: {motinha[0]}")
    sleep(1)