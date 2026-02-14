def descontos(dados):
    out = []
    ##TODO: Aplicar descontos


    
    
    ##Escreve o teu código aqui em cima!
    return out

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [("pc",400,"Eletrónicos"),("aspirador",100,"Eletrónicos"),("laca", 20,"Produtos de beleza"),("cadernos",15, "Produtos escolares")],
    [("relogio",100,"Eletrónicos"),("smart garrafa de água",25,"Eletrónicos"),("coluna",50,"Eletrónicos")],
    [("amendoas",3,"Comida"), ("lenços",1,"Produtos higiénicos"), ("maçã",1,"Fruta")]
]

##Isto são os resultados esperados para o teu código
resultados = [
    [("pc",360,"Eletrónicos"),("aspirador",90,"Eletrónicos"),("laca", 20,"Produtos de beleza"),("cadernos",15, "Produtos escolares")],
    [('relogio', 90, 'Eletrónicos'), ('smart garrafa de água', 22, 'Eletrónicos'), ('coluna', 45, 'Eletrónicos')],
    [('amendoas', 3, 'Comida'), ('lenços', 1, 'Produtos higiénicos'), ('maçã', 1, 'Fruta')]
]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = descontos(testes[i])
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