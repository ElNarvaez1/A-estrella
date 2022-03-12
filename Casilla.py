# Clase representativa para una casilla.
# Author: Narvaez Ruiz Alexis
class Casilla():

    """
        Constantes que definen el rol de la casilla, 
        podrian ser una de inicio, una Normal o la casilla de destino
    """
    ROL_INICIO = 'INICIO'
    ROL_DESTINO = 'DESTINO'
    ROL_NORMAL = 'NORMAL'
    ROL_BLOQUEADO = 'BLOQUEADO'
    PASO = 10

    # Constructor de la clase
    def __init__(self,keyStr,G = 0,H = 0,F = 0):
        """
            Construtor de la clase, inicializa 3 de los 4 argumentos,
            keyStr -> Es el nombre de la casilla,
            G,H,F -> Son los valores especificados en el video
        """
        
        self.__keyStr = keyStr 
        self.__G = G
        self.__H = H
        self.__F = F
        self.__rol = Casilla.ROL_NORMAL
        # Define que casilla es el origen. 
        self.__origin = None 
        # Coordenadas, se pueden evitar usando los diccionarios
        self.__x = 0
        self.__y = 0

    ## -------------------------------- GETTERS Y SETTERS --------------------------------
    ## Nota:::: Todo este codigo se puede evitar usando los diccionarios

    def getKey(self):
        return self.__keyStr 


    def setRol(self,rol):
        self.__rol = rol

    def getRol(self):
        return self.__rol

    def setX(self,x):
        self.__x = x
    
    def getX(self):
        return self.__x
        
    def setY(self,y):
        self.__y = y

    def getY(self):
        return self.__y

    def setOrigin(self,origin):
        self.__origin = origin

    def getOrigin(self):
        return self.__origin

    def setG(self,newG):
        self.__G = newG

    def getG(self):
        return self.__G

    def setH(self,newH):
        self.__H = newH
    
    def getH(self):
        return self.__H

    def setF(self,newF):
        self.__F = newF

    def getF(self):
        return self.__F

    def __str__(self):
        # return f"""Name: {self.__keyStr}, G: {self.__G}, F: {self.__F}, H: {self.__H}"""
        return f"""Name: {self.__keyStr}, x: {self.__x},y: {self.__y}"""