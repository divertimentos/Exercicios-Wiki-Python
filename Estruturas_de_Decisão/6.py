# Faça um Programa que leia três números e mostre o maior deles.

higher = 0

for num in range(1, 4):
    n = float(input(f"Digite um número ({num}/3: \n"))
    if n > higher:
        higher = n
print(f"Maior: {higher}")

