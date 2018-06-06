'''
Faça um programa para a leitura de duas notas parciais de um aluno. 

O programa deve calcular a média alcançada por aluno e apresentar:

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

soma = 0

for num in range(1, 3):
    nota = float(input(f"Nota {num}/2: \n"))
    soma += nota

media = (soma / num)

if media == 10:
    print("Aprovado com louvor.")
elif media >= 7:
    print("Aprovado.")
elif media < 7:
    print("Reprovado.")
