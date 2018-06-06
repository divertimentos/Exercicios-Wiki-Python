# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido

salario_hora = float(input("Quanto você ganha por hora? \n"))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? \n"))
salario_bruto = (((salario_hora * 8) * 5) * 4)
print("Salario bruto é: %s" %salario_bruto)

desconto_ir = ((salario_bruto * (11/100)))
print("Desconto IR:", desconto_ir)

desconto_inss = ((salario_bruto * (8/100)))
print("Desconto INSS:", desconto_inss)

desconto_sind  = ((salario_bruto * (5/100)))
print("Desconto Sindicato:", desconto_sind)

salario_liquido = (salario_bruto - (desconto_ir + desconto_sind + desconto_inss))
print("Salário líquido:", salario_liquido)
