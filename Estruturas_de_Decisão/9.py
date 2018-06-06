# Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
for i in range(1, 4):
    n = int(input(f"Digite um número ({i}/3): \n"))
    lista.append(n)

print(list(reversed(lista)))
