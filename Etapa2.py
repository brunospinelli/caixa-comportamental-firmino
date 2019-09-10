
def liberarRecompensa():
    print("->Libere 0,5 mL de recompensa\n")

def etapa2():
    nRepeticoes = 0
    while True:
        somEmitido = input("Qual o som emitido pelo animal (1 ou 2)? ")
        barraTocada = input("Qual a barra tocada pelo animal (D ou E)? ")

        if (somEmitido == "1" and barraTocada == "E") or (somEmitido == "2" and barraTocada == "D"):
            liberarRecompensa()
        else:
            print("->Não libere recompensa\n")
        
        nRepeticoes += 1

        if nRepeticoes == 50:
            tempoExperimento = int(input("Quanto tempo (em minutos) se passou desde o início do experimento? "))
            if tempoExperimento <= 30:
                print("O animal pode ir para a próxima fase!")
                return
            elif tempoExperimento > 30:
                print("Realize o treinamento novamente!")
                nRepeticoes = 0
