nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2
if nota1>10 or nota2>10:
    print("Nota inválida")
else:
    if media>=9:
        print("Passou com méritos")
    elif media>=8:
        print("Passou como se esperava")
    elif media>=6:
        print("Passou por pouco")
    else:
        print("Reprovado")
