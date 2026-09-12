"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""
    
#Ejercicio 1

class Cancion:
    #Constructores de la clase
    def __init__(self, nombre, duracion, genero):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    #Comandos  
    def establecerNombre(self, nombre):
        self.nombre = nombre

    def establecerDuracion(self, duracion):
        self.duracion = duracion

    def establecerGenero(self, genero):
        self.genero = genero
    
    #Consultas de la clase
    def obtenerNombre(self):
        return self.nombre
    
    def obtenerDuracion(self):
        return self.duracion
    
    def obtenerGenero(self):
        return self.genero
    