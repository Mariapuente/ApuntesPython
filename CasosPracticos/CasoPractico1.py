# Crear una funcion que nos muestre por pantalla un titulo y el nombre del autor
# Despues pedir un texto por pantalla y calcular su hash


def cabecera():
    print("""  
        ████████╗██╗████████╗██╗   ██╗██╗      ██████╗ 
        ╚══██╔══╝██║╚══██╔══╝██║   ██║██║     ██╔═══██╗
           ██║   ██║   ██║   ██║   ██║██║     ██║   ██║
           ██║   ██║   ██║   ██║   ██║██║     ██║   ██║
           ██║   ██║   ██║   ╚██████╔╝███████╗╚██████╔╝
           ╚═╝   ╚═╝   ╚═╝    ╚═════╝ ╚══════╝ ╚═════╝ 
                                            <MARIA PUENTE BENITO>
  
    """)

cabecera()
mensaje = input ("Introduce tu texto aqui: ")
hasValue = hash(mensaje)
print ("El hash del mensaje es: ", hasValue)