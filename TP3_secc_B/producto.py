"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""

#Ejercicio 1
# (incluye Ejercicio 9: atributos privados con Name Mangling)

class Producto:
    #contructor
    def __init__(self, nombre):
        self.__nombre = nombre
        
    #Consultas
    def obtenerNombre(self):
        return self.__nombre
    
    # Ejercicio 8
    def __str__(self):
        return str(self.obtenerNombre())
    
    def __eq__(self, other):
        return self.obtenerNombre() == other.obtenerNombre()
