# Funciones de calculo y comprobacion que necesita el algoritmo.

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
    
    positionOriginX = blockOrigin.getX() 
    positionOriginY = blockOrigin.getY()
    
    # Esquina superior izquierda  
    cornerLeftTop = {'x':positionOriginX - 1, 'y':positionOriginY - 1}
    for yTemp in range(cornerLeftTop['y'],cornerLeftTop['y'] + 3):
        for xTemp in range(cornerLeftTop['x'],cornerLeftTop['x'] + 3):
            # Necesitamos comprobar, si el origen puede tener casillas a la izquierda, 
            # sin desbordarse
            if (xTemp < limitMatrix_X) and (xTemp >= 0):
                if (yTemp < limitMatrix_Y) and (yTemp >= 0):
                    # Esta dentro del rango que puede ser admitido
                    neighbors.append(matrix[yTemp][xTemp])

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
        temp = False
        for elementoList2 in list2:
            if (elemento.getKey() == elementoList2.getKey()):
                temp = True
                break
        if not temp:
            listNew.append(elemento)
    return listNew
