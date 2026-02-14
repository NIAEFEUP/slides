def ordenar(tuplos):
    rf = []
    ##TODO: Ordenar os empregados



    return rf
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("Ana",3),("Pedro",4),("José",1)],
    [("Jorge",1),("Carlos",300000),("Érica",3)],
    [("Isaura",1),("Santiago",4),("Salvador",-20)]
]

##Isto são os resultados esperados para o teu código
resultados = [
    ["José","Ana","Pedro"],
    ["Jorge","Érica","Carlos"],
    ["Salvador","Isaura","Santiago"]
]


##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = ordenar(testes[i])
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