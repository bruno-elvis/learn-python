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