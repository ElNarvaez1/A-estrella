from operator import contains

matrix = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]
]
subMatrix = matrix[0:6]

print('Submatrix: ' + str(subMatrix))

columns = []

for columnsSub in subMatrix:
    # columnsSub is an Array
    columns.append(columnsSub[0:6])

print(columns)













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
