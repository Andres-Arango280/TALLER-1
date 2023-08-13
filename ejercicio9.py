

def imprimir_matriz(filas, columnas):
    contador = 1
    for i in range(filas):
        for j in range(columnas):
            print(contador, end=" ")
            contador += 1
        print()

if __name__ == "__main__":
    filas = 3
    columnas = 4

    imprimir_matriz(filas, columnas)

