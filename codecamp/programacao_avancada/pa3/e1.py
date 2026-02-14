import datetime

def funcionarios_datas_estacao(funcionarios):
    resultado = {
        "Inverno": [],
        "Primavera": [],
        "Verão": [],
        "Outono": []
    }

    # TODO

    return resultado

# Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("Maria Albertina", datetime.datetime(1994, 8, 20)), ("Carlos Mendes", datetime.datetime(2001, 4, 30))],
    [("Cristina Ferreira", datetime.datetime(2003, 11, 13))],
    [("Maria Albertina", datetime.datetime(1994, 8, 20)), ("João Baião", datetime.datetime(1990, 7, 1)), ("Fernando Mendes", datetime.datetime(1968, 1, 19))]
]

# Isto são os resultados esperados para o teu código
resultados = [
    {"Inverno": [], "Primavera": ["Carlos Mendes"], "Verão": ["Maria Albertina"], "Outono": []},
    {"Inverno": [], "Primavera": [], "Verão": [], "Outono": ["Cristina Ferreira"]},
    {"Inverno": ["Fernando Mendes"], "Primavera": [], "Verão": ["Maria Albertina", "João Baião"], "Outono": []}
]


# Podes ignorar o que vem abaixo desta linha
# É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = funcionarios_datas_estacao(testes[i])
        if tmp == resultados[i]:
            print("Teste ",i+1,": ✅",sep="")
        else:
            print("Teste ",i+1,": ❌",sep="")
            print("Esperado:",resultados[i])
            print("Obtido:",tmp)
    except Exception as e:
        print("Teste ",i+1,": ⚠️",sep="")
        print("Esperado:",resultados[i])
        print("Erro:",str(e))