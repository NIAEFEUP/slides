def descontos(dados):
    out = []
    ##TODO: Aplicar descontos
    for i in dados:
        if i[2] == "Eletrónicos":
            out.append((i[0],round(i[1]*0.9),i[2]))
        else:
            out.append(i)
    
    return out
    ##Escreve o teu código aqui em cima!
