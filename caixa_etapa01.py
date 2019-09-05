isAnimalHabituado = input ("O animal está habituado? (Não = 0, Sim = 1) ")


if isAnimalHabituado == '0':
    print ("Animal não habituado, continue o treinamento!")

else:

    distancia = 30

    distancia = int(input ("Qual a distância do animal? (cm) "))

    if distancia < 30:
        print ("Leberar 0,5ml de recompensa")        

    nToques = int(input("Quantas vezes o animal tocou as barras?"))

    if nToques == 20:
        print("O animal passou para a próxima etapa.")



