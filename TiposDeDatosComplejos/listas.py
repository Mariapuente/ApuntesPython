# su sintaxis es con [,...,...,...]

miLista = ['Hola mundo' , 2, 3 , 4, 'Adios mundo'] # Las listas se pueden componer de cualquier tipo de dato
print(miLista)

print(type(miLista))


# Podemos utilizar con ellas los operadores vistos anteriormente

miLista1 = ['Hola mundo' , 2, 3 , 4]

print(miLista == miLista1)
print(miLista1 in miLista) # El resultado es false porque no contiene una lista, si no los elementos
print('Hola mundo' in miLista) # Por eso aqui nos va a dar true

#Para concatenar listas lo hariamos con la suma, o la multiplicacion por un entero, como en los Strings

print(miLista + miLista1)

# Nuestra lista puede contener objetos totalmente iguales

miLista2 = [ 'texto', 'texto', 'texto', 'texto']
print(miLista2)

# Tambien pueden contener funciones

def miFuncion():
    return 3

miLista3 = [1,2, miFuncion(),4,5]
print(miLista3)

# Podemos acceder a los elementos a traves de la indexacion
# Utilizamos tanto la indexacion como el slicing y el stride
print(miLista1[2])
print(miLista1[0:3])
print(miLista1[0:4:2])

# PODEMOS UTILIZAR EL STRIDE PARA DARLE LA VUELTA A LA LISTA
print(miLista)
print(miLista[::-1])

# Si utilizamos la sintaxis [:] en las listas, nos devuelve la copia del objeto, pero no una referencia del objeto como en los Strings
print(miLista[:])

miLista4 = miLista[:]

print(miLista4 is miLista) # Nos da false porque no tienen el mismo id

print(id(miLista))
print(id(miLista4))

# Soportan muchos operadores en Python

lista5 = [1,2,3,4,5,6]
lista6 = [7,8,9,10,11,12]

print(lista5 + lista6) # La suma concatena

print(lista5 * 3 ) # La multiplicacion concatena la lista el numero de veces del entero por el que la multipliquemos 

print(min(lista5+lista6)) # Nos retorna el minimo valor de nuestras listas
print(max(lista5+lista6)) # Retorna el maximo valor de nuestras listas

print(len(lista6)) # Nos muestra la longitud de nuestras listas


# Las listas se pueden anidar, es decir una lista puede contener dentro listas que contengan listas y asi sucesivamente

lista7 = [1,2,3,[4,5,6,['Hola','Adios'],7,8,9],10,11,12]
print(lista7)

# Podemos eliminar elementos de las listas
del lista7[0]
print(lista7) # Observamos que se ha borrado el 1

#Para llegar a los elementos de las sublistas tenemos que utilizar la sintaxis [][]

print(lista7[2][3][1]) #Anidaremos tantos [] como sublistas haya

# Podemos utilizar el Slicing y el Stride para modificar elementos de nuestras listas, y no hace falta cambiarlos por el mismo numero de elementos

lista7[2][3] = 0

print(lista7) # Hemos cambiado la lista ['Hola', 'Adios'] por 0

