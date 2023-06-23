# Creacion de funciones personalizadas

def miFuncion (parametro1, parametro2):
    print(parametro1,"y", parametro2)

miFuncion(1,5)

miFuncion("Maria", "Alejandro")

# Podemos crear una funcion sin parametros

def miFuncion2 ():
    print("Hola mundo")

miFuncion2()

# Tambien podemos crear una funcion con valores por defecto

def miFuncion3(parametro1, parametro2 = "Valor por defecto"):
    print(parametro1,"y", parametro2)

miFuncion3(1)
miFuncion3("Maria")

# Aunque nuestro parametro3 tenga un valor por defecto podemos asignsrle otro valor

miFuncion3("Maria", "Alejandro")


# Podemos añadir un RETURN a la funcion para que retorne en ese mismo momento

def miFuncion4():
    print("Dentro de la funcion")
    return #Aqui directamente se corta la funcion
print ("Fuera de la funcion")
miFuncion4()

# Tambien despues del return podemos pedirle lo que queremos que nos retorne

def miFuncion5():
    num = print(10 + 15)
    return num

miFuncion5()