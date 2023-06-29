#Crea un diccionario que represente la agenda digital. Dentro de ese diccionario, crea otro diccionario
# por cada uno de los contactos que quieras almacenar en ella. Los contactos deben tener, al menos, los siguientes atributos:
#Nombre, dirección, email y teléfono.

agendaDigital ={
    'Maria Puente Benito': {
        'direccion': 'C/ Alcala',
        'email': 'enumerate@example.com',
        'telefono': 658457558
    },
    'Alejandro Perez Sainz': {
        'direccion': 'C/ Goya',
        'email': 'enumerate1@example.com',
        'telefono': 622347558
    },
    'Pepito Gonzalez Sanchez' :{
        'direccion': 'C/ Boltaña',
        'email': 'enumerate3@example.com',
        'telefono': 666522448
    }

}



# Implementa una función en Python que permita escribir en disco la agenda digital que has representado en el apartado anterior como un diccionario.

#agendaFichero = open( 'agendaDigital','w')  # Esto lo que ha hecho ha sido abrir un fichero nuevo que se guardara en mi disco.
#agendaFichero.write(str(agendaDigital)) 
#agendaFichero.close

# Lo que vamos a hacer es crear una funcion que haga todo esto 

def escribirAgenda(nombreAgenda, agenda_digital): #Lo que hacemos aqui es crear el fichero
    """
    Parametros posicionales:
    nombreAgenda: str que representa el nombre de la agenda en disco
    agenda_digital dict que representa la agenda digital y los contactos
    """
    agendaFichero = open( 'CasosPracticos/AgendaDigital/agendaDigital','w')  # Esto lo que ha hecho ha sido abrir un fichero nuevo que se guardara en mi disco.
    agendaFichero.write(str(agendaDigital)) 
    agendaFichero.close


# Implementa una función en Python que nos permita leer el fichero en el que has escrito la agenda digital y has almacenado en disco en el apartado anterior.

def leerAgenda(nombreAgenda):
    """
    Parametro nombreAgenda -- str que representa el nombre de la agenda en disco
    """
    agendaDigitalLectura = open(nombreAgenda, 'r')
    agendaDigital = agendaDigitalLectura.readlines() # Nos permite leer las lineas de nuestro fichero
    agendaDigitalLectura.close()
    return eval(agendaDigital[0]) # Nos devuelve la agenda que hemos almacenado en disco en forma de diccionario


# Crea una función en Python que solicite los datos de un nuevo contacto de la agenda por pantalla al usuario y cree una nueva entrada en nuestra agenda digital

def solicitarContactoAgenda():
    """ Solicita los datos de un nuevo contacto al usuario"""
    nombre = input('Introduce el nombre del contacto: ')
    direccion = input ('Introduce la direccion del contacto: ')
    email = input('Introduce el email del contacto: ')
    telefono = input('Introduce el telefono del contacto: ')
    #Aqui ya hemos definido las variables del diccionario 
    # Construimos un diccionario con los valores recibidos
    contacto ={
        'nombre' : nombre,
        'direccion' : direccion,
        'email' : email,
        'telefono' : telefono
    }
    return contacto

nuevoContacto = solicitarContactoAgenda()



def crearContacto(agendaDigital, nuevoContacto):
    """
    Parametros
    agendaDigital -- dict que representa la agenda digital existente
    nuevoContacto -- dict que representa un nuevo contacto

    """
    agendaDigital[nuevoContacto['nombre']] ={
        'direccion': nuevoContacto['direccion'],
        'email': nuevoContacto['email'],
        'telefono': nuevoContacto['telefono']
    }   
    return agendaDigital

crearContacto(agendaDigital, nuevoContacto)

# Implementa una función en Python que solicte por pantalla el nombre completo de un contacto de la agenda y,
#  a partir de ese nombre, nos proporcione el resto de información: dirección, email y teléfono...

def consultarContactoAgenda(agendaDigital):
    """
    Esta funcion consulta un contacto en la agenda"""
    nombre = input('Introduce el nombre completo del contacto: ')
    print('\n[+]', nombre)
    print('\tDireccion: ', agendaDigital[nombre]['direccion'])
    print('\tEmail: ', agendaDigital[nombre]['email'])
    print('\tTelefono: ', agendaDigital[nombre]['telefono'])

consultarContactoAgenda(agendaDigital) # Aqui consultamos un contacto de nuestra agenda


# Pon en común todas las funciones que has implementado en las secciones anteriores para mostrar la funcionalidad de tu agenda digital.
#CREA UN NUEVO CONTACTO EN LA AGENDA
agendaDigital = leerAgenda('CasosPracticos/AgendaDigital/agendaDigital')
nuevoContacto = solicitarContactoAgenda()
crearContacto(agendaDigital, nuevoContacto)
escribirAgenda("CasosPracticos/AgendaDigital/agendaDigital", agendaDigital)

# CONSULTA UN CONTACTO EXISTENTE

agendaDigital = leerAgenda('CasosPracticos/AgendaDigital/agendaDigital')
consultarContactoAgenda(agendaDigital)
