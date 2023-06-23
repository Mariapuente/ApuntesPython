# Los unarios lo que hacen es darle el valo negativo o positivo al numero

num = 10

print(+num)
print(-num)

# Suma y resta

num1 = 10
num2 = 23

suma = num1 + num2
print(suma)

resta = num2 - num1
print(resta)

restaNegativa = num1 - num2
print(restaNegativa)

# Podemos sumar y restar numeros float tambien

num3 = 1.5
num4 = 8.6

resta = num4 - num3
print(resta)

suma = num4 + num3
print(suma)

# Concatenacion de Strings

text1 = " Esta es la primera cadena de texto"
text2 = "esta es la segunda cadena de texto"

print(text1 + " y " + text2)

# Multiplicacion y division

num1 = 10
num2 = 5

multiplicacion = num1 * num2
print(multiplicacion)

division = num1 / num2
print(division) # La division siempre nos devuelve un float, sea numero entero o no para volverlo int tendriamos que hacerle un casting

print(int(division))

# Si multiplicamos un String por otro da error
# Si multiplicamos un String por un numero entero, nos repite ese string las veces que lo multipliquemos

multiText = "Texto" * 5
print(multiText)


# El modulo es el resto de la division entre numeros (float o enteros)
 
num1 = 10
num2 = 3

num3 = num1 % num2

print(num3)

# Para elevar a un numero lo representamos con **

num4 = num2 ** 6

print(num4)

# Si en queremos ver solo la parte entera de una division con decimales (no redondea, solo corta la parte entera) utilizamos // 
num4 = num1 / num2
num5 = num1 // num2
print(num4)
print(num5)