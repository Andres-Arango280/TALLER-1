#  Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada

def encontrar_extremos(lista):
    if not lista:
        return None, None 

    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero

    return maximo, minimo
  
lista_numeros = [5, 10, 3, 8, 1, 15]

maximo, minimo = encontrar_extremos(lista_numeros)
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)

