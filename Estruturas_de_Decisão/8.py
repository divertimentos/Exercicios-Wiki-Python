# Faça um programa que pergunte o preço de três produtos 
# e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

lowest = 0
cheapest = ""

for i in range(1, 4):
    prod = input(f"Nome do produto ({i}/3): \n")
    price = float(input(f"Preço do produto ({i}/3): \n"))

    if lowest == 0:  # Impedindo que o contador nunca saia do zero.
        lowest = price
        cheapest = prod
    
    if price < lowest:
        cheapest = prod
        lowest = price

print(f"Mais barato: {cheapest}.")
