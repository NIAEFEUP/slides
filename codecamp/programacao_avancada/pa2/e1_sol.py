def espionagem_empresarial(nossos_clientes, clientes_doutras_empresas):
    out = set()
    for i in nossos_clientes:
        if i in clientes_doutras_empresas:
            out.add(i)
    

    return out