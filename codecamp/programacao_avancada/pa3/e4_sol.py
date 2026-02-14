def encriptar(mensagem, chave):
    resultado = ""
    for caracter in mensagem:
        if caracter.isalpha():
            # Guardar se era maiúscula ou minúscula
            e_maiuscula = caracter.isupper()
            
            # Trabalhar com maiúsculas
            caracter = caracter.upper()
            
            # Calcular nova posição
            posicao = ord(caracter) - ord('A')
            nova_posicao = (posicao + chave) % 26
            novo_caracter = chr(nova_posicao + ord('A'))
            
            # Restaurar maiúscula/minúscula
            if not e_maiuscula:
                novo_caracter = novo_caracter.lower()
            
            resultado += novo_caracter
        else:
            # Manter espaços, números, pontuação
            resultado += caracter

    return resultado