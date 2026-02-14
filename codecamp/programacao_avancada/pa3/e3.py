import datetime

def verificar_ano_bissexto(funcionarios):
    resultado = []
    
    # TODO

    return resultado

# Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("Maria", datetime.datetime(1996, 8, 20)), ("Carlos", datetime.datetime(2001, 4, 30))],
    [
        ("João", datetime.datetime(2000, 9, 1)), ("Marco", datetime.datetime(2002, 3, 7)), 
        ("Diogo", datetime.datetime(1992, 3, 3)), ("Alice", datetime.datetime(1999, 10, 29)),
        ("Nuno", datetime.datetime(1976, 12, 5))
    ]
]

# Isto são os resultados esperados para o teu código
resultados = [
    ["Maria"],
    ["João", "Diogo", "Nuno"]
]


# Podes ignorar o que vem abaixo desta linha
# É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = verificar_ano_bissexto(testes[i])
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