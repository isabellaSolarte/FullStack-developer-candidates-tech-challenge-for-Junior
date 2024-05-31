#tercer reto
def minimo_cambio_no_creable(monedas):
    # Paso 1: Ordenar las monedas
    monedas.sort()
    print(monedas)
    # Paso 2: Inicializar la variable para llevar la cuenta de la menor cantidad de cambio que no podemos crear
    cambio_actual = 1
    
    # Paso 3: Iterar a través de las monedas ordenadas
    for moneda in monedas:
        # Si la moneda actual es mayor que la menor cantidad de cambio que no podemos crear, rompo el bucle
        if moneda > cambio_actual:
            break
        # De lo contrario, sumar el valor de la moneda al cambio actual
        cambio_actual += moneda
    
    # Paso 4: Devolver el resultado
    return cambio_actual

# Probar la función con el ejemplo proporcionado
monedas = [5, 7, 1, 1, 2, 3, 22]
print(minimo_cambio_no_creable(monedas))  # Salida: 20

monedas =  [1, 1, 1, 1, 1]
print(minimo_cambio_no_creable(monedas))  # Salida: 6

monedas =   [1, 5, 1, 1, 1, 10, 15, 20, 100]
print(minimo_cambio_no_creable(monedas))  # Salida: 55


