entrada = int(input("Digite um número entre 0 e 10: \n"))

while(entrada < 0 or entrada > 10):
    print("Você digitou um valor inválido!")
    entrada = int(input("Digite um número entre 0 e 10: \n"))
if entrada > 0 and  entrada < 11:
    print("O número %s é válido! Abrindo programa..." %entrada)
