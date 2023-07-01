# La sentencia break se utiliza para terminar de manera inmediata la ejecucion de un bucle

colores = ['rojo', 'verde', 'azul']
for color in colores:
    print(color)


for color in colores:
    print(color)
    break # Vemos como solamente ejecuta el bucle una vez hasta que llega al break


# La sentencia continue lo que hace es interrumpir la ejecucion actual

for color in colores:
    print(color)
    print("Esta sentencia  se ejecutará ya que va delante del continue")
    continue
    print("Esta sentencia nunca se ejecutará ya que va detras del continue")

for color in colores:
    continue
    print(color) # Nunca se ejecutará


# La sentencia pass se utiliza para que no nos de error una funcion, bucle... vacios cuando estamos empezando un programa

def miFuncion():
    pass # Como no se que voy a ejecutar en esta funcion, pongo pass y cuando ejecute la funcion no da error