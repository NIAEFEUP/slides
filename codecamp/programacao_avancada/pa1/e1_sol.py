def limpar_dados(dados):
    ##TODO: Limpar os dados
    out = ""

    for i in dados:
        if i.isalpha() or i == " ":
            out+=i

    return out
    ##Escreve o teu código aqui em cima!