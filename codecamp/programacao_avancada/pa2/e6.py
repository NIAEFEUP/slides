def contar_deps(dados):
    out = []
    ##TODO: Contar quem está em dois ou mais departamentos

    ##Escreve o teu código aqui em cima!
    return out


##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [
        ("Ana Silva", ["Recursos Humanos", "Vendas"]),
        ("Miguel Costa", ["TI"]),
        ("Sónia Rocha", ["Vendas"]),
        ("Afonso Dias", ["TI", "Logística", "Segurança"]),
        ("Inês Santos", ["Engenharia"]),
        ("Carla Antunes", ["Logística", "Finanças"]),
        ("Abel Ferreira", ["Finanças"]),
    ]
]

##Isto são os resultados esperados para o teu código
resultados = [["Ana Silva", "Afonso Dias", "Carla Antunes"]]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = contar_deps(testes[i])
        if tmp == resultados[i]:
            print("Teste ", i + 1, ": ✅", sep="")
        else:
            print("Teste ", i + 1, ": ❌", sep="")
            print("Esperado:", resultados[i])
            print("Obtido:", tmp)
    except Exception as e:
        print("Teste ", i + 1, ": ⚠️", sep="")
        print("Esperado:", resultados[i])
        print("Erro:", str(e))
