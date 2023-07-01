# Estructura de la sentencia if
# if <expresion>
#       <sentencia(s)>

num1 = 5
num2 = 10

num1 < num2 # Esta sentencia es True, siempre que sea asi, si lo metemos en el if, nos ejecutara lo que le pidamos despues

if num1 < num2:
    print('La sentencia se ejecuta porque es True')


# Lo podemos utilizar con cualquier tipo de dato

miLista = ['azul', 'verde', 'amarillo']

if 'amarillo' in miLista:
    print('El color se encuentra en nuestra lista')

miTupla = (1,2,3,4,5,6)

if miTupla[2] < 4:
    print('El valor ', miTupla[2], 'es menor que 4')

#La sentencia else, la metemos si lo que queremos es que si la sentencia es false, ejecute otra cosa distinta

miTupla = (1,2,3,4,5,6)

if miTupla[2] < 4:
    print('El valor ', miTupla[4], 'es menor que 4')
else:
    print('El valor', miTupla[4], 'es mayor que 4')

#La sentencia elif, es la que utilizamos como el switch de JAVA

nombres= ['Maria', 'Alejandro', 'Pedro', 'Sara']

if 'Juan' in nombres:
    print('Hola Juan')
elif 'Sonia' in nombres:
    print('Hola Sonia')
elif 'Carlos' in nombres:
    print('Hola Carlos')
elif 'Maria' in nombres:
    print('Hola Maria')
else:
    print('No existe el nombre en la lista')


# Tenemos que tener en cuenta que podemos poner la sentencia if en una sola linea

if 'Maria' in nombres: print('Que tal Maria')

# Operador condicional en  Python lo utilizamos de la siguiente manera

tiempo = 'lluvia'

print('Vamos', 'a la piscina' if tiempo == 'sol' else 'al cine')

tiempo = 'sol'

print('Vamos', 'a la piscina' if tiempo == 'sol' else 'al cine')