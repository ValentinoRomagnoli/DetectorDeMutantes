def isMutant(dna):
    rows = len(dna)
    cols = len(dna[0])

    # Verificar horizontalmente
    for i in range(rows):
        for j in range(cols - 3):
            if dna[i][j] == dna[i][j + 1] == dna[i][j + 2] == dna[i][j + 3]:
                return True

    # Verificar verticalmente
    for i in range(rows - 3):
        for j in range(cols):
            if dna[i][j] == dna[i + 1][j] == dna[i + 2][j] == dna[i + 3][j]:
                return True

    # Verificar diagonalmente (de izquierda a derecha)
    for i in range(rows - 3):
        for j in range(cols - 3):
            if dna[i][j] == dna[i + 1][j + 1] == dna[i + 2][j + 2] == dna[i + 3][j + 3]:
                return True

    # Verificar diagonalmente (de derecha a izquierda)
    for i in range(rows - 3):
        for j in range(3, cols):
            if dna[i][j] == dna[i + 1][j - 1] == dna[i + 2][j - 2] == dna[i + 3][j - 3]:
                return True

    # Si no se encuentra ninguna secuencia de cuatro letras iguales
    return False

# Ingreso de las filas de la matriz por teclado
dna = []
for _ in range(6):
    row = input("Ingrese una fila de la matriz: ")
    dna.append(row.upper())  # Convertir a mayúsculas para asegurar la comparación

# Verificar si es mutante
if isMutant(dna):
    print("Es un mutante.")
else:
    print("No es un mutante.")