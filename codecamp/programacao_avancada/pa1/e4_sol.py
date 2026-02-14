def avaliacao_funcionarios(tuplos):
    resultado = []
    rf = []
    n = len(tuplos)
    for (nome, avaliação) in tuplos:
        resultado.append((avaliação,nome))
    
    resultado.sort()
    for (avaliação,nome) in resultado:
            rf.append(nome)
    return rf
