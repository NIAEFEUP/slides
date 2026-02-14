def sala_secreta(dados):
    out = []
    ##TODO: Ver quem pode aceder à sala secreta


    
    ##Escreve o teu código aqui em cima!
    return out

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    {"Inês": {"Eletrotécnica", "Vendas"},"Maria": {"Mecânica"},"Mário": {"Informática", "Contabilidade"},"Ana": {"Informática", "Segurança", "Recursos Humanos"}},
    {"Rodrigo": {}, "Adelaide": {"Vendas", "Informática"}, "André": {"Segurança"}},
    {"Alfredo": {"Informática", "Segurança"}, "Albertina": {"Segurança", "Informática"}}
]

##Isto são os resultados esperados para o teu código
resultados = [
    ["Ana"],
    [],
    ["Alfredo","Albertina"]

]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = sala_secreta(testes[i])
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