def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[j] < lista[i]:
                lista[i], lista[j], = lista[j], lista[i]
    return lista
    
    
lista = [5,2,9,1,7]
lista_ord = ordenar(lista)
print("A lista ordenada é:", lista_ord)