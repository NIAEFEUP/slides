def encriptar(mensagem, chave):
    resultado = ""
    
    # TODO

    return resultado

# Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ["Reuniao as 15h", 5],
    ["Wjzsnft fx 15m", -5],
    ["VAIS SER DESPEDIDO", 15]
]

# Isto são os resultados esperados para o teu código
resultados = [
    "Wjzsnft fx 15m",
    "Reuniao as 15h",
    "KPXH HTG STHETSXSD"
]


# Podes ignorar o que vem abaixo desta linha
# É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = encriptar(testes[i][0], testes[i][1])
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