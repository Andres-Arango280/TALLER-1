import random

def generar_lista_aleatoria(cantidad_numeros, rango_inicial, rango_final):
    lista_aleatoria = [random.randint(rango_inicial, rango_final) for _ in range(cantidad_numeros)]
    return lista_aleatoria

def imprimir_lista(lista):
    for numero in lista:
        print(numero)

if __name__ == "__main__":
    cantidad_numeros = 10  # Puedes cambiar este valor según la cantidad de números que quieras generar
    rango_inicial = 1  # Puedes cambiar este valor para modificar el rango inicial de los números aleatorios
    rango_final = 100  # Puedes cambiar este valor para modificar el rango final de los números aleatorios

    lista_aleatoria = generar_lista_aleatoria(cantidad_numeros, rango_inicial, rango_final)
    imprimir_lista(lista_aleatoria)





