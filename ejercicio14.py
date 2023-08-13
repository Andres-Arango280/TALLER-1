#. Escribir una función que calcule la media aritmética de una lista de números.



entrada = (input("Ingrese los números separados por comas: "))


lista_numeros = [int(numero.strip()) for numero in entrada.split(",")]

cantidad = len(lista_numeros)
suma = sum(lista_numeros)
media = suma /  cantidad

print("la media es de: ",media)


