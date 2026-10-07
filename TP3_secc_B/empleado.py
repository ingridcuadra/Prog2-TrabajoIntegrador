"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""

#Ejercicio 2
# (incluye Ejercicio 9: atributos privados con Name Mangling)

class Empleado:
    #Atributos
    ESTADO_ALTA = 1
    ESTADO_BAJA = 2
    
    #contructor
    def __init__(self, nombres, apellidos):
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__numeroLegajo = None
        #ejercicio 3
        self.__estado = self.ESTADO_ALTA
    
    #Comandos
    def establecerNumeroLegajo (self, numeroLegajo):
        self.__numeroLegajo = numeroLegajo
    def establecerNombres (self, nombres):
        self.__nombres = nombres
    def establecerApellidos (self, apellidos):
        self.__apellidos = apellidos
    def establecerEstado (self, estado):
        self.__estado = estado
    
    #Consultas
    def obtenerNumeroLegajo (self):
        return self.__numeroLegajo
    def obtenerNombres (self):
        return self.__nombres
    def obtenerApellidos (self):
        return self.__apellidos
    def obtenerEstado (self):
        return self.__estado
    
    # Ejercicio 8
    def __str__(self):
        return str(self.obtenerNumeroLegajo())+" "+str(self.obtenerNombres())+" "+str(self.obtenerApellidos())+" "+str(self.obtenerEstado())
    
    def __eq__(self, other):
        return self.obtenerNumeroLegajo() == other.obtenerNumeroLegajo()
