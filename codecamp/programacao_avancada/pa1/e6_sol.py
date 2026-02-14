def gerar_email(dados):
    ##TODO: Gerar os emails
    out = []


    for i in dados:
        firstname = i.split()[0].lower()
        lastname = i.split()[-1].lower()
        out.append(firstname+lastname+"@corporate.com")



    return out
    ##Escreve o teu código aqui em cima!