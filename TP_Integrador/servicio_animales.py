import servicio_zoologicos

class ServicioAnimales:

    def obtener_animales_por_cuidador_principal(self, id_zoologico, id_cuidador_principal):
        zoologico = servicio_zoologicos.ServicioZoologicos().obtener_por_id(id_zoologico)
        
        if zoologico is None:
            return []
        
        id_cuidador = int(id_cuidador_principal)
        return [animal for animal in zoologico.obtener_animales()
                if animal.obtener_id_cuidador_principal() == id_cuidador]