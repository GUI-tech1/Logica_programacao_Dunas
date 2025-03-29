def cauculo():
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
    if op=="+":
        print(soma)
    if op=="-":
        print(sub)
    if op=="*":
        print(mult)
    if op=="/":
        print(div)
    if op=="**":
        print(pot)
    if op=="//":
        print(rdiv)
    return rei
while cauculo()!="n":
    cauculo()
print("ACABOU")

    
