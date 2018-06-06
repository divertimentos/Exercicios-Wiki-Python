a = int(input("Digite a população de A: \n"))
b = int(input("Digite a população de B: \n"))
anos = 0

if (a < b):
    while (b >= a):
        a = ((a * 3 / 100) + a)
        b = ((b * 1.5 / 100 + b))
        anos += 1
    print("Tempo decorrido: %s anos." %anos)
elif (a == b):
    print("As cidades têm populações idênticas.")
elif (a > b):
    print("A cidade A já ultrapassou B em número de habitantes.")
