import datetime

def estacao_funcionarios(funcionarios, input):
    resultado = []
    contagem = 0

    for f in funcionarios:
        mes = f[1].month
    
        if mes in (12, 1, 2):
            estacao = "Inverno"
        elif mes in (3, 4, 5):
            estacao = "Primavera"
        elif mes in (6, 7, 8):
            estacao = "Verão"
        elif mes in (9, 10, 11):
            estacao = "Outono"
        
        if estacao == input:
            resultado.append(f[0])
            contagem += 1

    return (resultado, contagem)