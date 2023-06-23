
# Los Strings en Python se representan mediante cadenas de texto
# Se representan con " " o ' '
text = "Esto es un String"
text1 = 'Esto tambien es un String'

# Podemos acceder a cualquier elemento de la cadena
# Tenemos que tener en cuenta que el primer caracter de la cadena siempre se situa en la posicion 0

print(text[3])

#Tambien podemos coger sub cadenas dentro de la cadena

print(text[0:5])

# Si quisieramos tambien podemos incorporar saltos dentro de la obtencion de la cadena

print(text[0:8:2]) # El ultimo valor entre corchetes son los saltos que damos para coger nuestra subcadena

#Para hacer Strings de lineas multiples

var = "Esto es un String \nde varias lineas \nen Python"
print(var)

var1 = """Esto tambien es 
un String de varias lineas
en Python"""

print(var1)

