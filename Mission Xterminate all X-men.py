def isMutant(adn):
    rows = len(adn)
    cols = len(adn[0])

    # Verificación del tamaño de la matriz
    if rows != 6 or cols != 6:
        print("Error: La matriz debe contener exactamente 6 filas y 6 columnas.")
        return False

    # Verificación de la longitud de cada fila
    for row in adn:
        if len(row) != 6:
            print("Error: Cada fila de la matriz debe tener una longitud de 6 caracteres.")
            return False

    # Verificación horizontalmente
    for i in range(rows):
        for j in range(cols - 3):
            if adn[i][j] == adn[i][j + 1] == adn[i][j + 2] == adn[i][j + 3]:
                return True

    # Verificación verticalmente
    for i in range(rows - 3):
        for j in range(cols):
            if adn[i][j] == adn[i + 1][j] == adn[i + 2][j] == adn[i + 3][j]:
                return True

    # Verificación diagonalmente (de izquierda a derecha)
    for i in range(rows - 3):
        for j in range(cols - 3):
            if adn[i][j] == adn[i + 1][j + 1] == adn[i + 2][j + 2] == adn[i + 3][j + 3]:
                return True

    # Verificación diagonalmente (de derecha a izquierda)
    for i in range(rows - 3):
        for j in range(3, cols):
            if adn[i][j] == adn[i + 1][j - 1] == adn[i + 2][j - 2] == adn[i + 3][j - 3]:
                return True

    # Si no se encuentra ninguna secuencia de cuatro letras iguales es una persona común y corriente (tira falso)
    return False

# Ingreso de las filas de la matriz por teclado
adn = []
for _ in range(6):
    while True:
        row = input("Ingrese una fila de ADN (por favor solo las letras A,T,C,G y solo 6 porque si no exploto uwu): ")
        row = row.upper()  # Convertir a mayúsculas para asegurar la comparación

        # Verificación de la validez de la fila
        if all(base in "ATCG" for base in row) and len(row) == 6:
            break
        else:
            print("Error: La fila debe contener solo las letras A, T, C, G y tener una longitud de 6 caracteres, intentelo nuevamente por favor.(profe le dije que no lo hiciera y lo hizo igual >:( si explotaba era su culpa))")

    adn.append(row)

# Verificar si es mutante o un simple mortal
if isMutant(adn):
    print("Es un mutante.")
else:
    print("No es un mutante.")
    # Espero que le guste mi trabajo, Saludos profe y que Dios lo bendiga
