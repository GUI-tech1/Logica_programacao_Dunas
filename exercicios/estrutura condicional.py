nota=float(input("qual a sua nota?"))
if nota<=0 or nota>10:
    print("Erro: Nota invalida. Digite um valor entre 0 e 10")
elif nota>=9:
    print("Aprovado")
elif nota>=6:
    print("Recuperação")
else:
    print("Reprovado")
