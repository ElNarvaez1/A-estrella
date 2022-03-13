# Author:  Narvaez Ruiz Alexis
# Cuadricula de ejemplo 
# A | B | C | D | E |
# F | G | H | I | J |
# K | L | M | N | Ñ |
# O | P | Q | R | S |
# T | U | V | W | X |


# ------------------------------ Explicacion de las variables ------------------------------
#
# F = G + H
# G -> Peso o costo necesario para llegar a una casilla,
#       los movimento rectos deben de pesar menos que los movimientos en diagonal.
#       = 
# H ->  Cantida de casillas hasta llegar al destino multiplicados por el
#       peso/costo de cada casilla(deben de ser contadas en lineas rectas) 
#       
#       N - > numero de casillas hasta llegar al destino
#       = (G * N)
#


# Necesitamos una lista abierta, dond e
# introducieromso los valores que analizaremos


from Casilla import Casilla
from Funciones import *


# Cuadriacula
matriz = [
    [Casilla('A'),Casilla('B'),Casilla('C'),Casilla('D'),Casilla('E')],
    [Casilla('F'),Casilla('G'),Casilla('H'),Casilla('I'),Casilla('J')],
    [Casilla('K'),Casilla('L'),Casilla('M'),Casilla('N'),Casilla('O')],
    [Casilla('P'),Casilla('Q'),Casilla('R'),Casilla('S'),Casilla('T')],
    [Casilla('U'),Casilla('V'),Casilla('W'),Casilla('X'),Casilla('Y')]
]
## Definimos los cuadros bloqueados
matriz[1][2].setRol(Casilla.ROL_BLOQUEADO)
matriz[2][2].setRol(Casilla.ROL_BLOQUEADO)
matriz[3][2].setRol(Casilla.ROL_BLOQUEADO)

# Bucles para asignar las coordenadas
for y in range(len(matriz)):
    limiteX = len(matriz[y])
    for x in range(limiteX):
        matriz[y][x].setX(x)
        matriz[y][x].setY(y)

# Definimos el origien y el destino
origen =  matriz[2][0] # Casilla k
destino =  matriz[2][4] # Casilla o
# Listas que necesita el programa
listAvailable = []
listUnavailable = []
position = None
 

# Repite mientras no hayas llegado al destino
position  = origen
while position != destino:
    #Ingresamaos la posicion actual a la lista cerrada.
    listUnavailable.append(position)
    
    # Necesitamos quitar de la lista abierta el elmento que ya se encuentra en la 
    # lista cerrada
    if position in listAvailable:
        listAvailable.remove(position)

    # Seleccionamos lo vecinos 
    vecinos = getNeighbors(matriz,position)
    # Aqui es donde necesitamos quitar a los vecinos que 
    # ya esten en la lista cerrada
    vecinos = filterTo(vecinos,listUnavailable)

    # Lista abierta temporal
    listAvailableTemp = []

    for casilla in vecinos:
        # Agregamos el vecino a la lista abierta
        if casilla not in listAvailable:
            listAvailable.append(casilla)

        # Preguntamos si no tiene una casilla de origen 
        if (casilla.getOrigin() is None):
            # Como esta libre le asignamos la casilla de Origen
            # (posicion actual) 
            casilla.setOrigin(position)

            # Falta corregir cuando es en diagonal o no
            casilla.setG(Casilla.PASO)

            distancia = getNumberBlockDistance(casilla,destino)
            casilla.setH(Casilla.PASO*distancia)
            # casilla.setF(casilla.getG()+casilla.getH())

    # Necesitamos saber cual de los elmentos de la lista abierta
    # tiene la "F"  menor
    #   Necesitamos ordenar primero.
    listAvailable = sorted(listAvailable,key = lambda block:block.getF())
    
    # Seleccionamos la primera casilla, ya que es la menor 
    nextBlock = listAvailable[0]

    # Asignamos la siguiente casilla como punto de origen
    position = nextBlock 
        





# Bucles para asignar las coordenadas
for y in range(len(listUnavailable)):
    print(listUnavailable[y])
    


# True -----
puntoActual = destino
while True:
    print(puntoActual.getKey())
    if (puntoActual.getOrigin() is None):
        break
    puntoActual = puntoActual.getOrigin()