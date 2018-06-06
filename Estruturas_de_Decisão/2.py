entrada = int(input("Descubra se seu número é positivo ou negativo: \n"))

if entrada > 0:
    print(entrada, "é positivo.")
elif entrada < 0:
    print(entrada, "é negativo.")
else:
    print(entrada, "é igual a zero.")
