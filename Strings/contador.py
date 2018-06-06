
string = input("Forneça uma string: \n")

quant = string.count("a")
quant = quant + string.count("e")
quant = quant + string.count("i")
quant = quant + string.count("o")
quant = quant + string.count("u")

print("A quantidade de vogais é:", quant)
