import datetime

def estacao_funcionarios(funcionarios, input):
    resultado = []
    contagem = 0

    # TODO

    return (resultado, contagem)

#Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ([("Maria", datetime.datetime(1994, 8, 20)), ("Carlos", datetime.datetime(2001, 4, 30))], "Primavera"),
    ([
        ("João", datetime.datetime(2000, 9, 1)), ("Marco", datetime.datetime(2002, 3, 7)), 
        ("Diogo", datetime.datetime(1992, 3, 3)), ("Alice", datetime.datetime(1999, 10, 29)),
        ("Nuno", datetime.datetime(1976, 12, 5))
    ], "Outono"),
    ([
        ("João", datetime.datetime(2000, 9, 1)), ("Marco", datetime.datetime(2002, 3, 7)), 
        ("Diogo", datetime.datetime(1992, 3, 3)), ("Alice", datetime.datetime(1999, 10, 29)),
        ("Nuno", datetime.datetime(1976, 12, 5))
    ], "Verão")
]

# Isto são os resultados esperados para o teu código
resultados = [
    (["Carlos"], 1),
    (["João", "Alice"], 2),
    ([], 0)
]


# Podes ignorar o que vem abaixo desta linha
# É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = estacao_funcionarios(testes[i][0], testes[i][1])
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