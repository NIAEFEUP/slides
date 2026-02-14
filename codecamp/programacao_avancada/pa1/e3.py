def inventario(produtos_necessarios, produtos_disponiveis):
    faltam = []
    disponiveis = []
    extra = []
    ##TODO: Inventário
    
    

    #Escreve o teu código aqui em cima!
    return faltam, disponiveis, extra

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    (["Fita cola","Agrafador"],["Fita cola","Cartão"]),
    (["Fita cola", "Agrafador", "Canetas", "Papel"],["Fita cola","Agrafador","Canetas","Papel","Computadores","Impressora"]),
    ([],["Lápis azul"])
]

##Isto são os resultados esperados para o teu código
resultados = [
    (["Agrafador"],["Fita cola"],["Cartão"]),
    ([],["Fita cola","Agrafador","Canetas","Papel"],["Computadores","Impressora"]),
    ([],[],["Lápis azul"])
]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = inventario(testes[i][0],testes[i][1])
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