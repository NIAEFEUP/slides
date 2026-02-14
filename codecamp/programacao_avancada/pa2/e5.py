def agradecer(dados):
    out = []
    ##TODO: Agradecer :)



    
    ##Escreve o teu código aqui em cima!
    return out

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("Ana Silva", "Recursos Humanos", 8),("Miguel Costa", "TI", 3),("Sónia Rocha", "Vendas", 12),("Inês Santos", "Engenharia", 5),("Ricardo Pereira", "Marketing", 1),("Carla Antunes", "Logística", 6), ("Afonso Dias", "TI", 4),("Abel Ferreira", "Finanças", 10)],

]

##Isto são os resultados esperados para o teu código
resultados = [
    ["Obrigado Ana Silva pelo teu serviço", "Obrigado Sónia Rocha pelo teu serviço", "Obrigado Carla Antunes pelo teu serviço", "Obrigado Abel Ferreira pelo teu serviço"],

]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = agradecer(testes[i])
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