"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")

#Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
#En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
#Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
#Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

class Coches:
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos

    def acelerar(self):
        self._velocidad += 1

    def frenar(self):
        #Crear los metodos setter y getters ._ estos metodos son importantes y necesarios en todos clases parra que el programador interactue con los valores de los atributos a traves de estps metodos... digamos que es la manera mas adecuada y recomendada
        #En teoria 
        self._velocidad -= 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color

    def setColor(self, color):
        self._color = color

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self, velocidad):
        self._velocidad = velocidad

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, asientos):
        self._Asientos = asientos

class Camiones(Coches): 



    def __init__(self, marca, color, modelo, velocidad, potencia, asientos,eje, capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__eje = eje
        self.__capacidadCarga= capacidadCarga

    def cargar(self,tipo_carga):
        print(f"El tipo de carga es:{tipo_carga}")
    
    def acelerar(self):
        self._velocidad += 1
        print(f"Estoy acelerando como un camion")

    def frenar(self):
        #Crear los metodos setter y getters ._ estos metodos son importantes y necesarios en todos clases parra que el programador interactue con los valores de los atributos a traves de estps metodos... digamos que es la manera mas adecuada y recomendada
        #En teoria 
        self._velocidad -= 1  
        print(f"Estoy frenando como un camion")

    def geteje(self):
        return self.__eje
    
    def seteje(self,eje):
        self.__eje =eje

    def getCapacidadCarga(self):
        return self.__capacidadCarga

    def setCapacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, potencia, asientos,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, potencia, asientos)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def transportar(self,num_pasajeros):
        print(f"El numero de pasajeros es: {num_pasajeros}")

    def acelerar(self):
            self._velocidad += 1
            print(f"Estoy acelerando como una camioneta")
    
    def frenar(self):
        #Crear los metodos setter y getters ._ estos metodos son importantes y necesarios en todos clases parra que el programador interactue con los valores de los atributos a traves de estps metodos... digamos que es la manera mas adecuada y recomendada
        #En teoria 
        self._velocidad -= 1  
        print(f"Estoy frenando como una camioneta")
    

    

