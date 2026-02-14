def inventario(produtos_necessarios, produtos_disponiveis):
    faltam = []
    disponiveis = []
    extra = []
    
    # Verificar o que falta e o que está disponível
    for produto in produtos_necessarios:
        if produto in produtos_disponiveis:
            disponiveis.append(produto)
        else:
            faltam.append(produto)
    
    # Verificar produtos extra
    for produto in produtos_disponiveis:
        if produto not in produtos_necessarios:
            extra.append(produto)
    
    return faltam, disponiveis, extra