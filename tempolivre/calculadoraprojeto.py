def cauculo():
    numero1=float(input("numero1:"))
    numero2=float(input("numero2:"))
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
    elif op=="-":
        print(sub)
    elif op=="*":
        print(mult)
    elif op=="/":
        print(div)
    elif op=="**":
        print(pot)
    elif op=="//":
        print(rdiv)
    else:
        print("Operação não conhecida")
    return rei
while cauculo()!="n":
    cauculo()
print("FINAL")

    
