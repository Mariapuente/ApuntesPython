# La sentencia del bucle while tiene la siguiente estructura
# while <expresion>:
#       <sentencia(s)>

numero = 10
while numero > 0:
    numero -= 1 # Importante añadir algo que decremente o incremente para que no se vuelva un bucle infinito
    print(numero)


# Como en el bucle FOR, tambien podemos añadir la sentencia ELSE.

numero = 10
while numero > 0:
    numero -= 1
    print(numero)
else:
    print('No hay mas numeros')

# Tambien podemos crear el bucle WHILE en una sola linea

num = 5
while num > 0: num -= 1; print(num) # ATENCION el ; importante ponerlo para que la sentencia funcione

