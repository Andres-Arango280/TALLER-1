# Escribir una función que calcule el factorial de un número dado.

def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


numero = 8

resultado = factorial_iterativo(numero)
print(f"El factorial de {numero} es {resultado}")
