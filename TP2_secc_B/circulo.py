"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""

#Ejercicio 5
class Circulo:
    #Atributos de clase
    PI = 3.1416
    
    #Constructores de la clase
    def __init__(self, radio):
        self.radio = radio
    
    #Comandos      
    def establecerRadio(self, radio):
        self.radio = radio
    
    #Consultas
    def obtenerRadio(self):
        return self.radio
    
    def obtenerDiametro(self):
        return self.radio * 2
    
    def obtenerArea(self):
        return self.PI * (self.radio ** 2)
    
    def obtenerPerimetro(self):
        return 2 * self.PI * self.radio
    
    
    