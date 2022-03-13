# Funciones de calculo y comprobacion que necesita el algoritmo.

from operator import contains
from Casilla import Casilla 

# Hay que cambiarle el nombre XD
def getNumberBlockDistance(casillaA,casillaB):
    """
        Regresa el numero de casillas/bloques, a las que se encuentra la casilla
        "A" de la casilla "B"
    """
    newX = 0
    newY = 0

    # Necesitamos comprobar, si el punto "A" esta por arriba del punto "B"
    if casillaA.getY() < casillaB.getY():
        newY = casillaB.getY() - casillaA.getY()
    else:
        # Significa que la casilla B esta por arriba
        newY = casillaA.getY() - casillaB.getY()

    # Necesitamos comporbar, si el punto "A" esta a la izquierda del punto "B"
    if casillaA.getX() < casillaB.getX():
        newX = casillaB.getX() - casillaA.getX()
    else:
        newX = casillaA.getX() - casillaB.getX()

    return (newX+newY)

# Cambiarle el nombre , creo que es un eror de traduccion XD
# Matrix -> Matriz principal de donde obtendra las casillas disponibles
def getNeighbors(matrix,blockOrigin):
    """"
        Regresa las casillas vecinas a partir del origen, 
        filtrando las que no son validas
    """
    # Nota ::: se puede reducir usando los rangos en los arreglos

    # Casillas vecinas
    neighbors = []

    # Limites de la matriz
    limitMatrix_X = len(matrix[0])
    limitMatrix_Y = len(matrix)
    
    # Esquina superior izquierda  
    cornerLeftTop = {'x':blockOrigin.getX() - 1,
                     'y':blockOrigin.getY() - 1}
    
    # Cortamos la matriz principal 
    corteInicialFilas = 0
    corteFinalFilas = 0

    if cornerLeftTop['y'] < 0:
         corteInicialFilas = 0
    else:
         corteInicialFilas = cornerLeftTop['y']
    if cornerLeftTop['y'] + 2 >= limitMatrix_Y:
        corteFinalFilas = limitMatrix_Y - 1
    else:
        corteFinalFilas = corteInicialFilas + 3
    if cornerLeftTop['y'] + 1 == 0:
        corteFinalFilas = 2

    # -------------------------------------------------------------------------------------------------------

    # Cortamos las filas 
    filas = matrix[corteInicialFilas:corteFinalFilas]

    # Calculamos el corte en las columnas
    corteInicialColumnas = 0
    corteFinalColumnas = 0

    if cornerLeftTop['x'] < 0:
        corteInicialColumnas = 0
    else: 
        corteInicialColumnas = cornerLeftTop['x']
    if cornerLeftTop['x'] + 2 >= limitMatrix_X:
        corteFinalColumnas = limitMatrix_X - 1
    else:
        corteFinalColumnas = corteInicialColumnas + 3
    if cornerLeftTop['x'] + 1 == 0:
        corteFinalColumnas = 2

    for fila in filas:
        # Fila es un arreglo
        elementos = fila[corteInicialColumnas:corteFinalColumnas] 
        for e in elementos:
            neighbors.append(e)

    #Filtramos las casillas que "SI" esten disponibles
    neighbors = filter(lambda block: block.getRol() is not Casilla.ROL_BLOQUEADO, neighbors)
    #Necesitamos quitar la casilla origen 
    neighbors = filter(lambda block: block.getKey() is not blockOrigin.getKey() ,neighbors)
    return list(neighbors)


def filterTo(list1,list2):
    """
        Regresa un lista con los elementos no repetidos en la en las listas.
        es decir quita los elementos que de la primera lista que ya se encuentren
        en la lista 2
    """
    listNew = []
    for elemento in list1:
        if elemento not in list2 :
            listNew.append(elemento)
    return listNew
