def sort_On(lista_sort):
    if(len(lista_sort)==1):
        return lista_sort
    else:
        n=len(lista_sort)
        for i in range(n // 2):
            lista_sort[i], lista_sort[n - 1 - i] = lista_sort[n - 1 - i], lista_sort[i]
        return lista_sort
     
def definir_lista(listN,S):
    nueva_lista=[]
    for i in listN:
        nuevo_numero = ''.join([digit for digit in str(i) if int(digit)<S])
        if nuevo_numero:
            nueva_lista.append(int(nuevo_numero))
    return sort_On(nueva_lista)


S = 5
lista_input = [60, 6, 5, 4, 3, 2, 7, 7, 29, 1] #Salida: [1, 2, 2, 3, 4, 0]
print( definir_lista(lista_input, S))
