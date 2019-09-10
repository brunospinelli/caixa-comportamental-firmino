def etapa1():
    isAnimalHabituado = input ("O animal está habituado? (Não = 0, Sim = 1) ")

    if isAnimalHabituado == '0':
        print ("Animal não habituado, continue a etapa de habituação!")
    else:
        distancia = 30
        for x in range (10):
            distancia = int(input ("Qual a distância do animal? (cm) "))

            if distancia < 30:
                print ("Liberar 0,5ml de recompensa.")
            else:         
                print ("Não libera a recompensa.")
        
        nToques = 0
        while nToques < 20:
            boolToca = bool(int((input("O animal tocou a barra?(Não = 0, Sim = 1)"))))

            if boolToca:
                print("Liberar 0,5ml de recompensa.")
                nToques = nToques + 1
            else:
                print ("Não libera a recompensa")
        print ("O experimento passou para a próxima etapa.")
