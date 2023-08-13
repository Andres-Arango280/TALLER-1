# Crear un programa que genere una lista de números pares entre 1 y 100. 




def generar_lista_pares():
    lista_pares = [numero for numero in range(1, 101) if numero % 2 == 0]
    return lista_pares

if __name__ == "__main__":
    lista_pares_generada = generar_lista_pares()
    print("Lista de números pares entre 1 y 100:")
    print(lista_pares_generada)





