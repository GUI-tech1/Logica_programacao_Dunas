

numero1=int(input("numero1:"))
numero2=int(input("numero2:"))
op=input("operação:")
rei=input("reiniciar?")
soma= numero1 + numero2
sub= numero1 - numero2
mult= numero1*numero2
div=numero1/numero2
rdiv=numero1//numero2
pot=numero1**numero2
#Adição
if op=="+":
    print(soma)

#Subtração
if op=="-":
    print(sub)

#Multiplicação
if op=="*":
    print(mult)

#Divisão
if op=="/":
    print(div)

#Potencia
if op=="**":
    print(pot)

#resto da divisão
if op=="//":
    print(rdiv)
def cauculo(caucular):
    global numero1=int(input("numero1:"))
    global numero2=int(input("numero2:"))
    global op=input("operação:")
    global rei=input("reiniciar?")
def reiniciar(resetar):
    return cauculo
if rei=="y":
    reiniciar