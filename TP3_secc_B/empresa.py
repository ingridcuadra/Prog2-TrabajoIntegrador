"""
ALUMNOS

BARBERIS Pablo Cesar
CUADRA VILCHEZ Ingrid Anneris
FERREIRA Maria Belen

"""

from empleado import Empleado
from producto import Producto

# Ejercicio 4
# (incluye Ejercicio 9: atributos privados con Name Mangling)

class Empresa:
      
    # Constructor
    def __init__(self, razonSocial):
        self.__productos = []
        self.__empleados = []
        self.__razonSocial = razonSocial
    
    # Comandos
    def establecerRazonSocial(self, razonSocial):
        self.__razonSocial = razonSocial
        
    def agregarProducto(self,producto):
        self.__productos.append(producto)
    
    def removerProducto(self,producto):
        self.__productos.remove(producto)
    
    # Ejercicio 5
    def altaEmpleado(self,empleado):
        if len(self.__empleados) == 0:
            legajo = 1
        else:
            legajo = max(e.obtenerNumeroLegajo() for e in self.__empleados) + 1
        
        empleado.establecerNumeroLegajo(legajo)        
        self.__empleados.append(empleado)
    
    # Ejercicio 6
    def bajaEmpleado(self,empleado):
        empleado.establecerEstado(Empleado.ESTADO_BAJA)
    
    # Consultas
    def obtenerRazonSocial(self):
        return self.__razonSocial
    
    def obtenerProductos(self):
        return self.__productos
    
    def obtenerEmpleadosDeAlta(self):
        # Ejercicio 7
        empleados_alta = []
        for empleado in self.__empleados:
            if empleado.obtenerEstado() == Empleado.ESTADO_ALTA:
                empleados_alta.append(empleado)
        return empleados_alta

    def obtenerEmpleadosHistorico(self):
        return self.__empleados
    
    # Ejercicio 8
    def __str__(self):
        return str(self.obtenerRazonSocial())+ "\n" + "\n".join([str(producto) for producto in self.obtenerProductos()])+ "\n" + "\n".join([str(empleado) for empleado in self.obtenerEmpleadosDeAlta()])
    
    def __eq__(self, other):
        return self.obtenerRazonSocial() == other.obtenerRazonSocial()