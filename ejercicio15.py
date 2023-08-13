#. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

caracter = input("Ingrese una palabra: ")

comparacion = caracter.lower()[::-1]

if caracter.lower() == comparacion:
    print("Su palabra es un palíndromo.")
else:
    print("Su palabra no es un palíndromo.")








