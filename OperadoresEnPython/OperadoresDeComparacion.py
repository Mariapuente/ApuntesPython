#Igualdad y desigualdad

num1 = 10
num2 = 10

print(num1 == num2)
print(num1 != num2)

#Podemos hacerlo tambien con Strings

text1 = "Hola mundo"
text2 = "Hola que tal "

print(text1 == text2)
print(text1 != text2)

# Si le preguntamos si un texto es mayor que el otro nos dira si es mayor el caracter que tengan diferentes (su valor en UNICODE)

print(text1 < text2)

print(ord('m')) # Aqui podemos ver el valor del caracter en la tabla unicode
print(ord('q'))

print(chr(115)) # En este caso nos dice que caracter tiene ese valor en la tabla unicode

# Tambien podemos comparar longitudes
 
print (len(text1) > len(text2))