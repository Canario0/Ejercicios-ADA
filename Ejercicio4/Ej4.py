# Formulas:
#           if(cad1[i]==cad2[j]): tablero[i,j]=tablero[i-1,j-1]
#           else: tablero[i,j]= min(tablero[i-1,j-1],tablero[i-1,j],tablero[i,j-1])+1
# Lo que viene a decir es que si los dos caracteres son iguales, las operaciones realizadas
# son las necesarias para llegar a ese punto(se encuentra en la diagonal) en caso contrario
# las operaciones necesarias son el mínimo de las que se ha realizado
# hasta ahora +1

# En cuanto a la implementación utilizo un diccionario que mantiene acceso constante a las posiciones
# y me permite generar la matriz sobre la marcha sin necesidad de
# generarla antes


def dinamic(cadena1, cadena2):
    tablero = dict()
    # Con esto decimos que los costes para formar cada una de las subcadenas
    # hasta la cadena total
    for i, _ in enumerate(" " + cadena2):
        tablero[0, i] = i
    for i, _ in enumerate(" " + cadena1):
        tablero[i, 0] = i
    for i, c1 in enumerate(cadena1, start=1):
        for j, c2 in enumerate(cadena2, start=1):
            if(c1 == c2):
                tablero[i, j] = tablero[i - 1, j - 1]
            else:
                tablero[i, j] = min(tablero[i - 1, j - 1], tablero[i - 1, j], tablero[i, j - 1]) + 1
    return tablero[len(cadena1), len(cadena2)]


print("Número de operaciones: ", dinamic("abcdefghijkl", "bcdeffghixkl"))
