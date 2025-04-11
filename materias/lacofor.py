#For quer dizer que para cada item dentro faça algo
# No exemplo o "i" é só uma variavel e pode ser substituida por qualquer coisa

# EXEMPLO 1 é o laço for com um range

for i in range(11): #O print vai ser do 1 ao 10 pq a contagem começa no 0
    print(i)

# EXEMPLO 2 é o laço for com uma lista
frutas=["banana", "maçã", "laranja"]
for f in frutas:
    print(f)
#Nesse exemplo o "0" é a onde inicia a contagem o "100" é o limite e o "10" é a diferença entre os numeros que vão no print
#O primeiro numero é o inicio, o segundo numero é o limite e o segundo é quantos numeros pula em cada contagem
#for q in range(0,100,10):
    #print(q)

#for g in range(1000):
    #print(f"Eu sou Guilherme {g+1}")

#Printa cada letra da variavel em string
nome="Guilherme"
for letra in nome:
    print(letra)