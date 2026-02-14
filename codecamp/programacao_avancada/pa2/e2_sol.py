def recuperar_password(passMod,dados):
    ##TODO: Recuperar passwords
    passOriginal = ""

    for i in passMod:
        if i not in dados:
            passOriginal+=str(i)
        else:
            passOriginal+=str(dados[i])
    




    return passOriginal
    ##Escreve o teu código aqui em cima!