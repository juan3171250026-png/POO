"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches

class Coches():
    def __init__(self,color,marca,velocidad):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad
        
    def acelerar(self):
        pass
    def frenar(self):
        pass
    def tocar_claxon(self):    
        pass


#Instanciar o crear objetos de la clase Coches


coche1=Coches("Rojo","Ferrari",300)
coche2=Coches("Azul","BMW",200)

print("El color del coche 1 es: {Coches.__color}")





