def verificar_p(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
    
texto = "Socorram me subi no onibus em Marrocos"

if verificar_p(texto):
    print(texto, "É um palindromo")
else:
    print(texto, "Não é um palindromo")