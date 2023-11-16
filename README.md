# DetectorDeMutantes
Legajo: 51638
alumno: Valentino Romagnoli
Email: redeemedwarriorblue@gmail.com
Descripción:
Este programa de detección de mutantes ha sido diseñado para identificar secuencias de ADN mutantes en una matriz de 6x6. Su objetivo es crucial: ayudar a Magneto a reclutar mutantes para enfrentarse a los X-Mens.

Cómo funciona:
El programa toma una matriz de strings como entrada, donde cada fila representa la secuencia de ADN. El usuario debe asegurarse de que la matriz cumple con los requisitos:

Debe contener exactamente 6 elementos.
Cada secuencia debe tener una longitud de 6 caracteres.
La secuencia no es sensible a las mayúsculas.
Si la matriz no cumple con estos requisitos, el programa informará al usuario para que reintroduzca los datos. (profe seguro ignoro la advertencia e intento explotar al pobre codigo)

El programa utiliza la técnica de comprensión de listas y splices para dividir la matriz en cadenas de 4 caracteres en direcciones diagonal, vertical y horizontal. Luego, compara estas cadenas con las secuencias de mutantes mediante un bucle simple.

Cómo usar el programa:

Descarga el archivo y abre una terminal en el mismo directorio.
Ejecute el archivo Mission Xterminate all X-men.py .
El programa te pedirá que ingreses la matriz de ADN fila por fila. Asegúrate de seguir las instrucciones y cumplir con los requisitos mencionados.(de no hacrlo alguien podria explotar)
Ejemplo:
Para verificar si una matriz es mutante, consideremos el siguiente ejemplo:

A T G C G A
C A G T G C
T T A T G T
A G A A G G
C C C C T A
T C A C T G
Este caso sería detectado como mutante por el programa.
