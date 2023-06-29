# Coleccion de elementos CLAVE -VALOR
# Su sintaxis es  {Key: value, Key2, value2, ...,KeyN: valueN}

miDiccionario = {
    'Nombre': 'Maria',
    'Apellidos': 'Puente Benito',
    'Edad': 29,
    'Pais': 'España'
}

print(miDiccionario)

# Para acceder a los elementos de un diccionario entre corchetes, en vez de poner el indice, pondremos la clave

print(miDiccionario['Nombre']) # Se debe, a que las claves de un diccionario tambien puede ser un tipo de dato numerico, y llevaria a confusion 

# Las claves tambien pueden ser tuplas

miDiccionario2 ={

    ('cero', 0) : 'zero',
    ('uno', 1) : 'uno',
    ('dos', 2) : 'dos',
    ('tres', 3) : 'tres'
}

print(miDiccionario2)
print(miDiccionario2[('cero', 0)]) # Para acceder siempre tenemos que utilizar la tupla entera

# Podemos modificar los elementos de un diccionario

miDiccionario2[('cero', 0)] = 'CERO'
print(miDiccionario2) # Vemos como ha cambiado 'zero' por 'CERO'

# Tambien podemos añadir elementos a la estructura

miDiccionario2[('cuatro',4)] = 'cuatro'
print(miDiccionario2) # Vemos como se ha añadido el cuatro 

# Dentro del diccionario puede haber cualquier tipo de dato, incluso diccionarios

miDiccionario3 = {
    'num': 10,
    'str': 'Hola mundo',
    'lista': [1,2,3,4],
    'tupla': (1,2,3,4),
    'dic': {'clave1': 'valor1','clave2':'valor2'}
}
print(miDiccionario3)

#Para acceder a los elementos de un diccionario dentro de otro, utilizaremos la misma sintaxis que en las listas [][]

print(miDiccionario3['dic']['clave2'])

#NO SE PUEDEN UTILIZAR LOS OPERADORES ARITMETICOS.

