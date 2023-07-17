from IPython.display import clear_output
class CuatroEnRaya:
    
    def __init__(self, filas, columnas): # Creamos el constructor al que le vamos a pasar el numero de filas y columnas que queremos que tenga nuestro tablero
        self._filas = filas
        self._columnas = columnas
        self._tablero = self.crearTablero()
        self._turno = None

    def crearTablero(self): # Crearemos el metodo crearTablero, que recogera el numero de filas y columnas del constructor
        tablero = [None] * self._filas
        for f in range(self._filas):
            tablero[f] = ['.'] * self._columnas
        return tablero
    
    def mostrarTablero(self): 
        for num in range(self._columnas):
            print(num, end = '  ')
        for fila in self._tablero:
            print('')
            for casilla in fila:
                print(casilla, end = '  ')
    
    def introducirFicha(self,columna, color):
        if columna >= self._columnas or columna < 0 :
            print('ERROR: Numero de columna fuera del rango')
        
        elif self._tablero[0][columna] != '.':
            print('ERROR: La columna esta llena de fichas')
        
        else:
            for fila in range(self._filas -1, -1, -1):
                if self._tablero[fila][columna] == '.':
                    self._tablero[fila][columna] = color
                    break  
            return self._tablero
            
    def _revisarFilas(self, color):

    #Recorremos las filas en busca de 4 en raya
        for r in range(self._filas):
            for c in range(self._columnas - 3):
                if self._tablero[r][c]  == color and self._tablero[r][c+1] == color and self._tablero[r][c+2] ==color and self._tablero[r][c+3] == color:
                    return True

    def _revisarColumnas(self, color):
    
    #Recorremos las columnas en busca de 4 en raya
        for c in range(self._columnas):
            for r in range(self._filas - 3):
                if self._tablero[r][c]  == color and self._tablero[r+1][c] == color and self._tablero[r+2][c] ==color and self._tablero[r+3][c] == color:
                    return True
            
    def _revisarDiagonalDerecha(self, color):
    
        for c in range(self._columnas -3):
            for r in range(self._filas -1, 2, -1):
                if self._tablero[r][c]  == color and self._tablero[r-1][c+1] == color and self._tablero[r-2][c+2] ==color and self._tablero[r-3][c+3] == color:
                    return True
    
    def _revisarDiagonalIzquierda (self, color):

    
        for c in range(self._columnas -1,2,-1):
            for r in range(self._filas -1,2,-1):
                if self._tablero[r][c]  == color and self._tablero[r-1][c-1] == color and self._tablero[r-2][c-2] ==color and self._tablero[r-3][c-3] == color:
                    return True

# Implementa una función que agrupe las cuatro funciones anteriores.

    def comprobarGanador (self, color):
        return self._revisarFilas(color) or self._revisarColumnas(color) or self._revisarDiagonalDerecha( color) or self._revisarDiagonalIzquierda(color)


    def jugar(self, player1 = 'X', player2='O'):
        self._turno = player2
        while True:
            self._turno = player1 if self._turno == player2 else player2 #Comprueba que player esta en turno ahora mismo y lo cambia directamente
          
            columna = int(input('Turno del jugador {}:'.format(self._turno)))#Con format introducimos lo que queramos dentro de los corchetes
            self.introducirFicha(columna, self._turno)
            
            clear_output(wait = False)
            if self.comprobarGanador(self._turno):
                print('\n\n Ganador el jugador {} !! \n\n'.format(self._turno))
                self.mostrarTablero()
                break
            self.mostrarTablero()        
juego = CuatroEnRaya(6,7)
juego.jugar()
