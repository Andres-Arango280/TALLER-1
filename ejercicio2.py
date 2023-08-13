#Escribir una función que calcule el área de un círculo dado su radio


def Calcular_Area (radio):
    pi = 3.14159
    area = pi * (radio**2)
    return area 

radio_circulo = 26

area_Circulo = Calcular_Area(radio_circulo)
print ("El área del círculo con radio", radio_circulo, "es:", area_Circulo  )



