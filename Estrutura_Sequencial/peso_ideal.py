genero = -1

while genero != 0:
    genero = int(input("Digite '1' se você é homem e '2' se você é mulher: \n"))

    #Fórmula homem:

    if genero == 1:
        print("Você selecionou homem.")
        #Peso ideal (Fórmula de Lorentz):
        k = 4
        peso_atual = int(input("Digite seu peso: \n"))
        h = float(input("Qual a sua altura? (em centímetros) \n"))
        p_ideal = ((h - 100) - (h - 150) / k)

        #Índice de Massa Corporal (IMC):

        h = (h / 100)
        imc = (peso_atual / (h ** 2))
        print("Seu Índice de Massa Corporal é: %s" %imc)

        #Grau de obesidade:

        if (imc < 18.5):
            print("Abaixo do peso ideal")
        elif (imc >= 18.5 and imc < 24.9):
            print("Peso normal.")
        elif (imc >= 25 and imc < 29.9):
            print("Acima do peso (sobrepeso)")
        elif (imc >= 30 and imc < 34.9):
            print("Obesidade grau I")
        elif (imc >= 35 and imc < 39.9):
            print("Obesdade grau II")
        elif (imc >= 40):
            print("Obesidade grau III")
        else:
            print("Você é um alienígena.")

        #Resultado:

        print("Seu peso ideal é: %s" %p_ideal)
        print("Seu IMC é: %s" %imc)
        break

    #Fórmula mulher:

    elif genero == 2:
        print("Você selecionou mulher.")
        #Peso ideal (Fórmula de Lorentz):
        k = 2
        peso_atual = int(input("Digite seu peso: \n"))
        h = float(input("Digite sua altura (em centímetros): \n"))
        p_ideal = ((h - 100) - (h - 150) / k)

        #Índice de Massa Corporal (IMC):

        h = (h / 100)
        imc = (peso_atual / (h ** 2))
        print("Seu Índice de Massa Corporal é: %s" %imc)

        #Grau de obesidade:

        if (imc < 18.5):
            print("Abaixo do peso ideal")
        elif (imc >= 18.5 and imc < 24.9):
            print("Peso normal.")
        elif (imc >= 25 and imc < 29.9):
            print("Acima do peso (sobrepeso)")
        elif (imc >= 30 and imc < 34.9):
            print("Obesidade grau I")
        elif (imc >= 35 and imc < 39.9):
            print("Obesdade grau II")
        elif (imc >= 40):
            print("Obesidade grau III")
        else:
            print("Você é um(a) alienígena.")

        #Resultado:

        print("Seu peso ideal é: %s" %p_ideal)
        print("Seu IMC é: %s" %imc)
        break
