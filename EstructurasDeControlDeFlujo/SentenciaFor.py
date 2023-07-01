# Su estructura es 
# for <variable> in <iterable>:
#       <sentencia(s)>

colores = ['verde', 'azul', 'rojo']
for color in colores: #Lo que hacemos es asignar un nombre a la variable que sera cada uno de los elementos de la lista
    print(color)

# Los objetos iterables se comprueban de la siguiente manera

print(iter([1,2,3,4]))

# Un iterador se va a corresponder con un objeto dentro de Python que nos va a devolver valores uno a uno
#  cuando utilicemos la función next() que viene implementada por defecto.

lista = ['rojo', 'azul', 'amarillo']
#ext(lista) #Aqui nos da error porque no es un iterador, pero podemos hacer el casting

listaIterador =iter(lista) #Aqui ya hemos hecho a nuestra lista iterador

print(next(listaIterador))
#Nos va a dar siempre un elemento de la lista, y si lo volvemos a poner nos dara el siguiente, ya que antes guarda el elemento en un espacio en nuestro programa

# Podemos poner la sentencia ELSE en el bucle FOR pero no se suele usar

for color in ['azul', 'verde', 'rojo']:
    print(color)
else:
    print('El bucle ya no tiene mas colores')


# Existe la sentencia RANGE, que lo que hace es darnos los valores desde el minimo hasta el maximo de un rango
print(range(5))
print(list(range(5)))

print(list(range(5,15))) #Siempre uno menos del maximo que pongamos

# Este range lo podemos utilizar para crear listas

miLista = range(10,25)

for num in miLista:
    print(num)

    