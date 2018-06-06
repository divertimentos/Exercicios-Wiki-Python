# Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas 
# e o preço total.

print("Este é o programa Loja de Tintas.")
area = 100
cobertura = area / 3
cobertura = (round(cobertura, ))
print("Para pintar %d metros quadrados, serão necessários %s litros" % (area, cobertura))
lata = 18 #litros
quantidade_latas = (cobertura // lata)
print("São necessárias %s latas" %quantidade_latas)
preco_latas = quantidade_latas * 80
print("O preço total de latas necessárias é igual a:", preco_latas)
