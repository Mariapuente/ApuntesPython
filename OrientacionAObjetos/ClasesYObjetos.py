# La sintaxis de una clase es la siguiente
class Coche:
    #El metodo __init__() es el constructor del objeto, por el que pasamos las variables que van a tener todos los objetos que tengamos
    def __init__(self, modelo, potencia, consumo):
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._kmActuales = 0 #Este es un valor por defecto ya que todos los objetos comenzaran con 0 kmActuales
        self._combustible = 'l/100KM'
    
    def especificaciones(self):
        print('Modelo:', self._modelo,
              '\nPotencia:', self._potencia,
              '\nConsumo:', self._consumo, self._combustible)
    
    def actualizarKm(self, kilometros):
        self._kmActuales = kilometros
    
    #Podemos extender la funcionalidad de nuestra clase creando un metodo que ejecute varias operaciones

    def consumoTotal(self):
        consumoTotal = (self._kmActuales / 100)* self._consumo
        print('El consumo total del vehiculo es:', consumoTotal, 'litros')

bmw = Coche('e46',250,12) 
bmw.especificaciones()
bmw.actualizarKm(15000)
print(bmw._kmActuales)
bmw.consumoTotal()

#Vamos a crear nuestra clase bateria
# Esta clase, la tenemos que meter siempre antes de la clase donde la vayamos a incluir, ya que tendremos que crear antes el objeto 
class Bateria:
    def __init__(self, capacidad, tipoPila, numPilas, peso):
        self._capacidad = capacidad
        self._tipoPila = tipoPila
        self._numPilas = numPilas
        self._peso = peso

    def especificaciones(self):
        print('Capacidad:', self._capacidad,
              '\nTipo de pila:', self._tipoPila,
              '\nNumero de pilas:', self._numPilas,
              '\nPeso de la bateria:', self._peso, 'Kgs') 

teslaBateriaModelS = Bateria(80,2170,203136,480)

# En este caso, si queremos registrar un coche electrico, no nos cuadran ciertos datos, por lo tanto crearemos una clase hija que herede del padre

class CocheElectrico(Coche):
    """Esta clase representa a un coche electrico"""

    def __init__(self, modelo, potencia, consumo, bateria):
        super().__init__(modelo, potencia, consumo)
        self._combustible = 'Kwh/100Km' # Aqui estamos modificando el tipo de combustible que tendran todos los coches electricos
        self._bateria = bateria

    def detallesBateria(self):
        self._bateria.especificaciones() #Tenemos que crear una clase bateria, en la que metamos objetos que luego nos serviran para nuestra clase CocheElectrico

tesla = CocheElectrico('tesla model 3', 250, 10, teslaBateriaModelS)
tesla.especificaciones()
tesla.detallesBateria()

