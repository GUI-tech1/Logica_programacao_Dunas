#Listas
cidades=["fortaleza","Sobral","Canide"]
print(cidades)

#Adcionar algo em uma parte da lista
#no caso do exemplo o 0 é a posição que vai ser inserida e representa a primeira posição da lista
cidades.insert(0,"Canidezinho")
print(cidades)

#Adcionar algo no final da lista
cidades.append("Redenção")
print(cidades)

#remover algo pelo index
cidades.pop(1)#O número dentro do pop é a posição do elemento que vai ser apagado
print(cidades)

#remover algo pelo nome
cidades.remove("Canide")
print(cidades)

#Mostra o tamanho da lista
print(len(cidades))

#Limpa completamente a lista
cidades.clear()
print(cidades)