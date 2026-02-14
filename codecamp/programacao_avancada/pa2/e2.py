def recuperar_password(passMod,dados):
    ##TODO: Recuperar passwords
    passOriginal = ""

    return passOriginal
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    ("ahdvhvhau",{"a":2, "v":9,"u":5}),
    ("abcdefghijklmnop",{"a":1,"k":0}),
    ("Ckrlpm",{"k":4,"p":0,"m":5})
]

##Isto são os resultados esperados para o teu código
resultados = [
    "2hd9h9h25",
    "1bcdefghij0lmnop",
    "C4rl05"
]


##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = recuperar_password(testes[i][0],testes[i][1])
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