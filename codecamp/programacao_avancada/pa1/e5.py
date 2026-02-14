def remover_duplicados(dados):
    ##TODO: Remover os duplicados
    out = []
    




    return out
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    [['Inês', 'Afonso','Sónia','Miguel'],['Samuel', 'Carla', 'Afonso', 'António'],['Ana', 'Inês', 'Abel']],
    [["Isaura", "Isaltino", "Iolanda"], ["Iara", "Isaura", "Irene"], ["Irene", "Iara", "Isaura"], ["Igor", "Isaac", "Ivan"]],
    [["Carlos","Carlos","Carlos","Carlos","Carlos"],["Carlos","Carlos","Carlos","Carlos","Carlos","Carlos","Carlos"],["Carlos"]]
]

##Isto são os resultados esperados para o teu código
resultados = [
    ['Inês', 'Afonso', 'Sónia', 'Miguel', 'Samuel', 'Carla', 'António', 'Ana', 'Abel'],
    ["Isaura", "Isaltino", "Iolanda", "Iara", "Irene", "Igor", "Isaac", "Ivan"],
    ["Carlos"]

]


##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = remover_duplicados(testes[i])
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