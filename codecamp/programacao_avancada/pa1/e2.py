def validar(passwords):
    passwords_validas = []
    ##TODO: Validar as passwords
    


    
    ##Escreve o teu código aqui em cima!
    return passwords_validas

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ["palavra passe","MonaLisa1234!","Je aime la france 2","0 meu amigo Carlo$","1aB!","1aB!               "],
    ["eabshbjabjasA", "Palsºnlasaey", "Abc1!234", "12345678", "Seguranca!", "Louvre2026", "Admin@123", "p@ssword1", "A1#b2"],
    ["PORTUGAL@2026", "qwertyuiop", "!!11AAaa", "Zorra$99", "12345@ABC", "solução123", "Mestre#01", "C0mplex@", "A", "SenhaSuperDificil", "GiroRápido!1", "1@A2#B3$", "........"]

]

##Isto são os resultados esperados para o teu código
resultados = [
    ["MonaLisa1234!","0 meu amigo Carlo$","1aB!               "],
    ["Abc1!234", "Admin@123"],
    ["PORTUGAL@2026", "!!11AAaa", "Zorra$99", "12345@ABC", "Mestre#01", "C0mplex@", "GiroRápido!1", "1@A2#B3$"]


]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = validar(testes[i])
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