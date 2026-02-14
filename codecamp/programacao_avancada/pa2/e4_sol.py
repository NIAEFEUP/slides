def sala_secreta(dados):
    out = []
    ##TODO: Ver quem pode aceder à sala secreta

    for i in dados:
        permissoes = dados[i]
        if "Informática" in permissoes and "Segurança" in permissoes:
            out.append(i)
    
    
    ##Escreve o teu código aqui em cima!
    return out