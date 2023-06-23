# No compara si los valores de los objetos son iguales o no, si no, si son el mismo objeto
# O si tienen mejor dicho, el mismo identificador

text1 = "Cadena de texto"
text2 = "Cadena de texto"

print (text1 is  text2)

print(id(text1))
print(id(text2))

