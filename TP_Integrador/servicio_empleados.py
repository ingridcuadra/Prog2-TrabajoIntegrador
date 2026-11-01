import servicio_zoologicos

class ServicioEmpleados:

    def obtener_cuidadores_principales(self, id_zoologico):
        zoologico = servicio_zoologicos.ServicioZoologicos().obtener_por_id(id_zoologico)
        
        if zoologico is None:
            return []
        
        id_cuidador_principal= {animal.obtener_id_cuidador_principal() 
                                for animal in zoologico.obtener_animales()}
        
        return [empleado for empleado in zoologico.obtener_empleados()
                if empleado.obtener_id() in id_cuidador_principal]
        
