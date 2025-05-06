def cauculo():
    print("selecione a operação desejada:")
    print("1. soma")
    print("2. subtração")
    print("3. multiplicação")
    print("4. divisão")
    print("5. potenciação")
    print("6. divisão inteira")
    print("7. sair")
    op=int(input("operação:"))
    if op==7:
        exit()
    A=float(input("digite o primeiro numero:"))
    B=float(input("digite o segundo numero:"))
    soma= A + B
    sub= A - B
    mult= A*B
    div=A/B
    rdiv=A//B
    pot=A**B
    if op=="1":
        print(soma)
    elif op=="2":
        print(sub)
    elif op=="3":
        print(mult)
    elif op=="4":
        print(div)
    elif op=="5":
        print(pot)
    elif op=="6":
        print(rdiv)
    else:
        print("Operação não conhecida")
while True:
    cauculo()     

    
