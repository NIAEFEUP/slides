import datetime

def funcionarios_datas_estacao(funcionarios):
    resultado = {
        "Inverno": [],
        "Primavera": [],
        "Verão": [],
        "Outono": []
    }

    for f in funcionarios:
        mes = f[1].month

        if mes in (12, 1, 2):
            resultado["Inverno"].append(f[0])
        elif mes in (3, 4, 5):
            resultado["Primavera"].append(f[0])
        elif mes in (6, 7, 8):
            resultado["Verão"].append(f[0])
        elif mes in (9, 10, 11):
            resultado["Outono"].append(f[0])

    print(resultado)