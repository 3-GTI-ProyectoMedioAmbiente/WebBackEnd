import json
#-----------------------------------------------------------------------------------
# @author: Juan Carlos Hernandez Ramirez
#Fecha: 14/10/2021
#-----------------------------------------------------------------------------------

class Medicion:
    def __init__(self,id, medicion, fecha, hora, localizacion_lat, localizacion_lon):
        self.id = id
        self.medicion = medicion
        self.fecha = fecha
        self.hora = hora
        self.localizacion_lat = localizacion_lat
        self.localizacion_lon = localizacion_lon

## Convierte la clase Medicion en JSON (string)
    def toJson(self):
        json = {
            "id": self.id,
            "medicion": self.medicion,
            "fecha": "{}".format(self.fecha),
            "hora": "{}".format(self.hora),
            "localizacion_lat": self.localizacion_lat,
            "localizacion_lon": self.localizacion_lon
            }
        return json