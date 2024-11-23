import requests
from random import sample

class Recomendaciones_DA:
    def __init__(self):
        self.contenidos_url = "http://localhost:8081/api/contenidos"

    def obtener_todos_los_contenidos(self):
        try:
            # Llamada al microservicio para obtener todos los contenidos
            response = requests.get(self.contenidos_url)
            response.raise_for_status()
            return response.json(), response.status_code
        except requests.RequestException as e:
            print(f"Error al obtener todos los contenidos: {e}")
            return {"message": "Error al obtener todos los contenidos"}, 500

    def recomendaciones_aleatorias(self, id_usuario, num_recomendaciones):
        try:
            # Obtener todos los contenidos de la base de datos
            contenidos_vistos, status_code = self.obtener_todos_los_contenidos()
            if status_code != 200:
                return contenidos_vistos, status_code

            # Seleccionar un número aleatorio de contenidos
            if not contenidos_vistos:
                return {"message": "No se encontraron contenidos en la base de datos"}, 500

            num_recomendaciones = min(num_recomendaciones, len(contenidos_vistos))
            recomendaciones = sample(contenidos_vistos, num_recomendaciones)

            return recomendaciones, 200
        except Exception as e:
            print(f"Error al obtener recomendaciones aleatorias: {e}")
            return {"message": "Error al obtener recomendaciones aleatorias"}, 500