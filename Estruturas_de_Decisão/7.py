# Faça um Programa que leia três números e mostre o maior e o menor deles.
highest = lowest = 0

for i in range(1, 4):
    n = int(input(f"Digite um número ({i}/3): \n" ))

    if n > highest:
        highest = n
        
    if lowest == 0:  # Impedindo que o contador nunca saia do zero
        lowest = n
    
    if n < lowest:
        lowest = n

print(f"Maior: {highest}.")
print(f"Menor: {lowest}.")
