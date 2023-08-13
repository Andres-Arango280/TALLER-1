#  Crear una función que convierta grados Fahrenheit a grados Celsius

def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius

grados_fahrenheir = 120

conversion = fahrenheit_a_celsius(grados_fahrenheir)

print ("los grados ", grados_fahrenheir,"fahrenheir  equivalen a ", conversion," grados celcius " )