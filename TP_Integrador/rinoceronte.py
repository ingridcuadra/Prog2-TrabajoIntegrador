
import animal

class Rinoceronte (animal.Animal):
    
    def __init__(self, id, nombre, id_cuidador_principal, largo_cuerno):
        super().__init__(id, nombre, id_cuidador_principal);
        self.__largo_cuerno = largo_cuerno

    def establecer_largo_cuerno(self, largo_cuerno):
        self.__largo_cuerno = largo_cuerno

    def obtener_largo_cuerno(self):
        return self.__largo_cuerno
    
    def __str__(self):
        return (f"ID: {self.obtener_id()}, "
                f"Nombre: {self.obtener_nombre()}, "
                f"ID Cuidador Principal: {self.obtener_id_cuidador_principal()}, "
                f"Largo de Cuerno: {self.obtener_largo_cuerno()}")
    