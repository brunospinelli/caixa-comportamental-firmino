
def liberarRecompensa():
    print("->Libere 0,5 mL de recompensa")


def isBarraCorreta(somEmitido, barraTocada):
    if (somEmitido == 1 and barraTocada == "E") or (somEmitido == 2 and barraTocada == "D"):
        liberarRecompensa()


def isExp50x30Min(nRepeticoes, tempoExperimento):
    if nRepeticoes == 50 and tempoExperimento <= 30:
        print("O animal pode ir para a próxima fase!")