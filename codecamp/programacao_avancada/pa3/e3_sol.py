import datetime

def verificar_ano_bissexto(funcionarios):
    resultado = []
    for f in funcionarios:
        ano_bissexto = False
        ano = f[1].year

        if ano % 4 == 0:
            if ano % 100 == 0:
                if ano % 400 == 0:
                    ano_bissexto = True
            ano_bissexto = True
        
        if ano_bissexto:
            resultado.append(f[0])

    return resultado