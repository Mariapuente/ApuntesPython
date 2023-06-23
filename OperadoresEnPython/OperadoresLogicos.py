# modifican y unen expresiones evaluadas en contexto booleano para crear condiciones mas complejas

num = 5

# El operador not invierte el valor que nos devuelve una expresion
print (num < 10)

print(not num < 10)

# El operador or mira si alguna de las consultas se cumplen para devolver un true

print( num < 10 or num > 5)

# El operador and lo que hace es que mira si se cumplen TODAS las consultas para devolver un True

print( num < 10 and num >5)
