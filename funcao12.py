def calcular_raiz(numero, precisao=0.0001):
    raiz = numero/2
    while abs(numero - raiz**2) > precisao:
        raiz = (raiz + numero/raiz)/2
    return raiz
    
numero =25
raiz = calcular_raiz(numero)
print("A raiz quadrada de", numero, "é", raiz)

print(abs(-5))