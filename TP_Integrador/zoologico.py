

class Zoologico:
    
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre
        self.__animales = []
        self.__empleados = []

        
    
    def establecer_id(self, id):
        self.__id = id
    
    def establecer_nombre(self, nombre):
        self.__nombre = nombre
    
    def agregar_animal(self, animal):
        self.__animales.append(animal)
        
    def remover_animal(self, animal):
        
        if animal in self.__animales:
            self.__animales.remove(animal)
    
    def agregar_empleado(self, empleado):
        self.__empleados.append(empleado)
    
    def remover_empleado(self, empleado):
        
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)

    def obtener_id(self):
        return self.__id
    
    def obtener_nombre(self):
        return self.__nombre
    
    def obtener_animales(self):
        return self.__animales
    
    def obtener_empleados(self):
        return self.__empleados
    
    def __eq__(self, other):
        
        if isinstance(other, Zoologico):
            return self.obtener_id() == other.obtener_id()
        return False
    
    def __str__(self):
        animales_str = ', '.join(str(animal) for animal in self.obtener_animales())
        empleados_str = ', '.join(str(empleado) for empleado in self.obtener_empleados())
        
        return (f"ID: {self.obtener_id()}, "
                f"Nombre: {self.obtener_nombre()}, "
                f"Animales: [{animales_str}], "
                f"Empleados: [{empleados_str}]")    