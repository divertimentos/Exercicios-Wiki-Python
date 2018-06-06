nome = input("Digite seu nome: \n")
nome = nome.upper()
nome = reversed(list(nome))

for i in nome:
    print(i, end = "")
