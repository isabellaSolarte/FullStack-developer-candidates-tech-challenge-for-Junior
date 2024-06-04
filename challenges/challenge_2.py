#segundo reto
def cuadrados_ordenados_en_rango(arr, S):
    # Definir el límite superior concatenando S dos veces
    limite_superior = int(str(S) * 2)
    print("Limite superior: " + (str(S) * 2))
    
    # Elevar al cuadrado los elementos y filtrar los que están fuera del rango
    cuadrados_filtrados = [ x * x for x in arr if 0 <= x * x <= limite_superior]
    return ordenar_lista(cuadrados_filtrados)
    
def ordenar_lista(cuadrados_filtrados):
    for i in range(1, len(cuadrados_filtrados)):
        clave = cuadrados_filtrados[i]
        j = i - 1
        while j >= 0 and clave < cuadrados_filtrados[j]:
            cuadrados_filtrados[j + 1] = cuadrados_filtrados[j]
            j -= 1
        cuadrados_filtrados[j + 1] = clave

    return cuadrados_filtrados    
   #[5, 1, 4, 2, 3] clave 1, j = 0 [5, 5, 4, 2, 3], j = -1   [1, 5, 4, 2, 3]


# Ejemplo de uso
array = [1, 2, 3, 5, 6, 8, 9]
S = 5
print(cuadrados_ordenados_en_rango(array, S))  # Salida: [1, 4, 9, 25, 36, 64]
