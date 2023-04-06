def calcular_media(nota):
    total = sum(notas)
    media = total / len(notas)
    return media
    

notas = [7.5,8,6.5,9]
media = calcular_media(notas)
print("A média é:", media)