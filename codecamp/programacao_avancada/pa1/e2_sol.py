def validar(passwords):
    passwords_validas = []
    caracteres_especiais = "!@#$"
    
    for password in passwords:
        # Verifica o comprimento mínimo, 8
        if len(password) < 8:
            continue
        
        # Verifica se tem pelo menos uma maiúscula
        maiuscula = False
        for caracter in password:
            if caracter.isupper():
                maiuscula = True
                break
        
        # Verifica se tem pelo menos um número
        numero = False
        for caracter in password:
            if caracter.isdigit():
                numero = True
                break
        
        # Verifica se tem pelo menos um caractere especial
        especial = False
        for caracter in password:
            if caracter in caracteres_especiais:
                especial = True
                break
        
        # Se cumprir todos os requisitos, adiciona à lista
        if maiuscula and numero and especial:
            passwords_validas.append(password)
    
    return passwords_validas
