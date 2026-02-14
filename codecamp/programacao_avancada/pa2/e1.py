def espionagem_empresarial(nossos_clientes, clientes_doutras_empresas):
    out = set()
    ##TODO: Espionagem empresarial
    

    return out
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ({"Joana", "Pedro", "Henrique", "Carlos"},{"Joana", "Elísio", "Henrique", "Santos"}),
    ({"Alberto","Nuno","Edite","Francisco"},{"Albertina","Nuno","Edite","Francisca"})
]

##Isto são os resultados esperados para o teu código
resultados = [
    {"Joana","Henrique"},
    {"Nuno","Edite"}
]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = espionagem_empresarial(testes[i][0],testes[i][1])
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