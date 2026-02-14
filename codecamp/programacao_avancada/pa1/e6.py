

def gerar_email(dados):
    ##TODO: Gerar os emails
    out = []



    return out
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ["Ana Faria Meireles", "Pedro José Vidal", "Manuel Silva", "Diogo Moreira Vaz"],
    ["Jorge Restivo", "Diogo Fernandes", "Rita Pereira"],
    ["Alberto Silva", "Pedro Souto"],
    ["Salvador Maria Pilar", "Francisco de Lencastre", "Duarte Xavier de Bragança Teles","Carlos Carlos"]
]

##Isto são os resultados esperados para o teu código
resultados = [
    ['anameireles@corporate.com', 'pedrovidal@corporate.com', 'manuelsilva@corporate.com', "diogovaz@corporate.com"],
    ["jorgerestivo@corporate.com","diogofernandes@corporate.com","ritapereira@corporate.com"],
    ["albertosilva@corporate.com","pedrosouto@corporate.com"],
    ["salvadorpilar@corporate.com","franciscolencastre@corporate.com","duarteteles@corporate.com","carloscarlos@corporate.com"]
]


##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = gerar_email(testes[i])
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

