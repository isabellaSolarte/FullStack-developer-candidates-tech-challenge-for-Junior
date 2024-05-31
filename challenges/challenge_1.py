#empieza el reto :D

def definir_lista(lst, s):
    def organizar_insercion(resultado, num):
        #Organizo por inserción el número en la lista result.
        for i in range(len(resultado)):
            if num > resultado[i]: #Si el número es mayor a algún elemento de la lista, se inserta en esa posición.
                resultado.insert(i, num)
                return
        resultado.append(num) #Si el número es menor a todos los elementos de la lista, se agrega al final.
    
    resultado = []
    for numero in lst:
        nuevo_numero = ''.join([digito for digito in str(numero) if int(digito) < s])
        if nuevo_numero:  # Ingresa solo si new_number no está vacío
            organizar_insercion(resultado, int(nuevo_numero))
    return resultado

# Ejemplo de uso
s = 5
lst = [1, 2, 3, 4, 5, 6]
list_resultado = definir_lista(lst, s)
print(list_resultado)  # Output:  [5, 4, 3, 2, 1]