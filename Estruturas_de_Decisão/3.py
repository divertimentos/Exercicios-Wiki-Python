entrada = input("Digite masculino ou feminino: \n")
entrada = entrada.upper()

if (entrada[0] == "M"):
    print("Masculino.")
elif (entrada[0] == "F"):
    print("Feminino")
else:
    print("Sexo não definido.")
