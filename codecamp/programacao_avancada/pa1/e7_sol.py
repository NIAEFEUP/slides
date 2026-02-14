def converter_dinheiro(dados):
    ##TODO: Converter o dinheiro 
    out = []

    for i in dados:
        out.append((i[0],round(i[1]/1.15,2)))

    return out
    ##Escreve o teu código aqui em cima!