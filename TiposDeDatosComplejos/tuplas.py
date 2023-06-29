# Su sintaxis es (..., ..., ...)

miTupla = (1, 2, 3, 4, 5, 6, 7)
print(type(miTupla))

# Funcionan de la misma manera que las listas 

miTupla1 = ( 'Hola', 1,2,3,4,5, 'Adios')
print(miTupla1)

print(miTupla1[2])

# La diferencia es que son inmutables

 # miTupla[1] = 0  NOS DA ERROR YA QUE NO SE PUEDEN MODIFICAR SUS ELEMENTOS

# Para crear una tupla con un unico dato numerico, la sintaxis será (...,)

miTuplaDeUnDato = (5,) # Si no lo interpretaria como un entero
print(type(miTuplaDeUnDato))

# Cuando creamos una tupla, la podemos desempaquetar en el mismo numero de variables como elements contenga

miTuplaDesempaquetada = (1,2,3,4,5)
num1, num2, num3, num4, num5 = miTuplaDesempaquetada

print(num1,num3, num5)

# Cuando en una funcion retornamos tipo de datos numericos, retornamos tuplas

def miFuncion():
    return (5,6,7)

print(miFuncion())
print(type(miFuncion()))

