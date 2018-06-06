string1 = input("Digite a primeira string: \n")
string2 = input("Digite a segunda string: \n")

if string1 != string2:
    tamanho1 = len(string1)
    tamanho2 = len(string2)
    print(string1)
    print(string2)
    print("O tamanho da primeira string é: %s." %tamanho1)
    print("O tamanho da segunda string é: %s" %tamanho2)
    print("As strings têm tamanhos diferentes.")
else:
    print("As duas strings são idênticas.")
