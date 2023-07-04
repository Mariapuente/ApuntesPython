

# Implementa una función que genere un tablero nuevo. 
#El tablero no debe ser complejo, para representarlo, utiliza una lista con varias listas anidadas

def crearTablero(filas, columnas):
    """Crea el tablero del juego
    Parametros posicionales:
    Filas -- int que representa el numero de filas del tablero
    Columnas -- int que representa el numero de columnas del tablero
    """
    tablero = [None] * filas #Lo igualamos a [None], porque lo que queremos es que salga vacio
    for f in range(filas):
        tablero[f] = ['.'] * columnas
    return tablero

# Una vez implementada la función para crear el tablero, 
# implementa otra función que permita imprimir el tablero por 
# pantalla de manera que el resultado sea similar al que se muestra en la imagen anterior.

def mostrarTablero(tablero):
    #Sacar por pantalla la cabecera
    for num in range(len(tablero[0])):
        print(num, end = '  ')
    #Sacar por pantalla el tablero
    for fila in tablero:
        print(' ')
        for casilla in fila:
            print(casilla, end= '  ')

#Implementa una función que permita introducir una nueva ficha en el tablero. 
# Para ello, ten en cuenta varias condiciones importantes, como, por ejemplo, que la columna 
# no se encuentre fuera del rango o que la columna no se encuentre llena de fichas.

def introducirFicha(tablero, columna, color):
    if columna >= len(tablero[0]) or columna < 0:
        print('ERROR: Numero de columna fuera del rango')
        return
    elif tablero[0][columna] != '.':
        print('ERROR: La columna esta llena de fichas')
        return
    else:
        for fila in range(len(tablero)-1, -1, -1):
            if tablero[fila][columna] == '.':
                tablero[fila][columna] = color
                return tablero

#Implementa cuatro funciones que permitan 
# verificar si se ha realizado cuatro en raya en horizaonal, vertical o diagonal.

def revisarFilas(tablero, color):
    # Obtenemos el numero de filas y columnas
    numFilas = len(tablero)
    numColumnas = len(tablero[0])
    #Recorremos las filas en busca de 4 en raya
    for r in range(numFilas):
        for c in range(numColumnas - 3):
            if tablero[r][c]  == color and tablero[r][c+1] == color and tablero[r][c+2] ==color and tablero[r][c+3] == color:
                return True

def revisarColumnas(tablero, color):
    # Obtenemos el numero de filas y columnas
    numFilas = len(tablero)
    numColumnas = len(tablero[0])
    #Recorremos las columnas en busca de 4 en raya
    for c in range(numColumnas):
        for r in range(numFilas - 3):
            if tablero[r][c]  == color and tablero[r+1][c] == color and tablero[r+2][c] ==color and tablero[r+3][c] == color:
                return True
            
def revisarDiagonalDerecha(tablero, color):
        # Obtenemos el numero de filas y columnas
    numFilas = len(tablero)
    numColumnas = len(tablero[0])
    
    for c in range(numColumnas -3):
        for r in range(numFilas -1, 2, -1):
            if tablero[r][c]  == color and tablero[r-1][c+1] == color and tablero[r-2][c+2] ==color and tablero[r-3][c+3] == color:
                return True
    
def revisarDiagonalIzquierda (tablero, color):
        # Obtenemos el numero de filas y columnas
    numFilas = len(tablero)
    numColumnas = len(tablero[0])
    
    for c in range(numColumnas -1,2,-1):
        for r in range(numFilas -1,2,-1):
            if tablero[r][c]  == color and tablero[r-1][c-1] == color and tablero[r-2][c-2] ==color and tablero[r-3][c-3] == color:
                return True

# Implementa una función que agrupe las cuatro funciones anteriores.

def comprobarGanador (tablero, color):
    return revisarFilas(tablero,color) or revisarColumnas(tablero, color) or revisarDiagonalDerecha(tablero, color) or revisarDiagonalIzquierda(tablero,color)



#Implementa un menu de juego que solicite a los usuarios que introduzcan una ficha por turnos. 
# Ten en cuenta que esta acción debe repetirse hasta que uno de los dos usuarios gane el juego o 
# se acaben las casillas disponibles para introducir fichas.

from IPython.display import clear_output
tablero = crearTablero(6,7)
turno = 'X'
siguienteTurno = '0'
while True:
    turno = siguienteTurno
    mostrarTablero(tablero)
    if turno == 'X':
        columna = int(input('Turno del rojo: '))
        siguienteTurno = '0'
    elif turno == '0':
        columna = int(input('Turno del amarillo: '))
        siguienteTurno = 'X'
    introducirFicha(tablero,columna,turno)
    clear_output(wait=False)
    if comprobarGanador(tablero, turno):
        print('Ganador : jugador', turno)
        mostrarTablero(tablero)
        break
        