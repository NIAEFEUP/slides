def converter_dinheiro(dados):
    ##TODO: Converter o dinheiro 
    out = []



    return out
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("Pc",900),("Telemóvel",500),("Aspirador",900)],
    [("Pastel de nata", 1), ("Pastel de nada", 0), ("Bolo de chocolate", 10)],
    [("Cão",10),("Gato",20),("Cobra",100), ("Carlos", 9999999999999)]
]

##Isto são os resultados esperados para o teu código
resultados = [
    [("Pc",782.61),("Telemóvel",434.78),("Aspirador",782.61)],
    [('Pastel de nata', 0.87), ('Pastel de nada', 0.0), ('Bolo de chocolate', 8.7)],
    [('Cão', 8.7), ('Gato', 17.39), ('Cobra', 86.96), ('Carlos', 8695652173912.17)]
]


##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = converter_dinheiro(testes[i])
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