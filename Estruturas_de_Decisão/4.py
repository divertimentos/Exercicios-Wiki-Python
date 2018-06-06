'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vogais = ["A", "E", "I", "O", "U"]
word = str(input("Descubra se a letra digitada é vogal ou consoante: \n")).strip().upper()

if word[0] in vogais:
    print(f"A letra {word[0]} é uma vogal.")
else:
    print(f"A letra {word[0]} não é uma vogal.")
