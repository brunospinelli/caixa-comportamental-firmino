
def liberarRecompensa():
    print("->Libere 0,5 mL de recompensa")

def etapa2():
    somEmitido = input("Qual o som emitido pelo animal (1 ou 2)? ")
    barraTocada = input("Qual a barra tocada pelo animal (D ou E)? ")

    if (somEmitido == "1" and barraTocada == "E") or (somEmitido == "2" and barraTocada == "D"):
        liberarRecompensa()
    
    nRepeticoes = input("Quantas vezes o experimento foi repetido? ")
    tempoExperimento = input("Quanto tempo (em minutos) se passou desde o início do experimento? ")

    if nRepeticoes == "50" and tempoExperimento <= "30":
        print("O animal pode ir para a próxima fase!")
    else:
        print("Realize o treinamento novamente!")
