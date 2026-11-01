
class Empleado:
    
    def __init__(self, id, nombres, apellidos):
        self.__id = id
        self.__nombres = nombres
        self.__apellidos = apellidos
        
    def establecer_id(self, id):
        self.__id = id
    
    def establecer_nombres(self, nombres):
        self.__nombres = nombres
        
    def establecer_apellidos(self, apellidos):
        self.__apellidos = apellidos
    
    def obtener_id(self):
        return self.__id
    
    def obtener_nombres(self):
        return self.__nombres
    
    def obtener_apellidos(self):
        return self.__apellidos
    
    def __str__(self):
        return (f"ID: {self.obtener_id()}, "
                f"Nombres: {self.obtener_nombres()}, "
                f"Apellidos: {self.obtener_apellidos()  }")
        
    def __eq__(self, other):
        
        if isinstance(other, Empleado):
            return self.obtener_id() == other.obtener_id()
        return False
    