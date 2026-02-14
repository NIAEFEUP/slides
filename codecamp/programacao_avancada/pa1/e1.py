def limpar_dados(dados):
    ##TODO: Limpar os dados
    return ""
    ##Escreve o teu código aqui em cima!

##Podes ignorar o que vem abaixo desta linha

##Isto são os dados de input que vão ser usados para testar o teu código
testes = [
    "B321321a521n521521an233211as",
    "223F3ei321j$##o321a/da##",
    "M32aç321ãs 321e C321ebola312s",
    "3920189047218075893270589718973892173'213125164312684381243821438921748149448921439217321Carlos438921483941289342198438921738921734821934891243892173892418937421897321",
    "3218930218930218321!!!!()()",
    "",
    "G1ir0o!Rápid0o",
    "iOf3ertas_$$$",
    "Joga#2026n0o_Carrinho",
    "K-Legal_v.9.9",
    "Loja&Virtu4al",
    "Meu**_Achado_888",
    "NaSu4aCasa_!!!",
    "OutletOnline%",
    "Pede&Leva_+",
    "QueroMais99",
    "Rede**deOfertas**_v1",
    "SóVantagens€€€",
    "Tudo**_Online**_24/7**",
    "Universo**daCompra_#",
    "Vem**deZap**_>>",
    "Web**Mania404",
    "Zuum!!!000",
    "Acelera_v8",
    "Bússola**SW180",
    "Clareza_100%",
    "Destino**Certo->",
    "Elo**deValor_2026",
    "Firma&Cia",
    "GeraValor$$",
    "Habilit**_001",
    "InovaAçãoX",
    "Junta#1",
    "K-riar****",
    "Lógica**_4.0",
    "Mestre_Yod@",
    "NorteVerdadeiro!!!",
    "Orion_-77-",
    "Plenitude_MAX",
    "Q-Conecta**_@",
    "Raiz******10",
    "Sinergia**Total!!!",
    "Trama**&Net",
    "Unus******01",
    "Vetor_[X]",
    "Zagaia******Z"

    
]

##Isto são os resultados esperados para o teu código
resultados = [
    "Bananas",
    "Feijoada",
    "Maçãs e Cebolas",
    "Carlos",
    "",
    "",
    "GiroRápido",
    "iOfertas",
    "JoganoCarrinho",
    "KLegalv",
    "LojaVirtual",
    "MeuAchado",
    "NaSuaCasa",
    "OutletOnline",
    "PedeLeva",
    "QueroMais",
    "RededeOfertasv",
    "SóVantagens",
    "TudoOnline",
    "UniversodaCompra",
    "VemdeZap",
    "WebMania",
    "Zuum",
    "Acelerav",
    "BússolaSW",
    "Clareza",
    "DestinoCerto",
    "ElodeValor",
    "FirmaCia",
    "GeraValor",
    "Habilit",
    "InovaAçãoX",
    "Junta",
    "Kriar",
    "Lógica",
    "MestreYod",
    "NorteVerdadeiro",
    "Orion",
    "PlenitudeMAX",
    "QConecta",
    "Raiz",
    "SinergiaTotal",
    "TramaNet",
    "Unus",
    "VetorX",
    "ZagaiaZ"

]

##É usado para testar se o teu código funciona
for i in range(len(testes)):
    try:
        tmp = limpar_dados(testes[i])
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