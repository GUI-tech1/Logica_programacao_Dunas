#quando usar o input se não for para caracteres é nescessario usar, int(), em caso de numeros inteiros e ,float(), em caso de decimais
numero= int(input("Quanto:"))
nome=input("Oque:")
if numero==10 and nome=="batatas":
    print("Você tem 10 batatas")
if numero>10 and nome=="batatas":
    print(f"Você tem batatas suficientes e vão sobrar {numero-10} batatas")
if numero<10 and nome=="batatas":
    print("Você não tem batatas suficientes")
if nome!="batatas":
    print("ERROR")

