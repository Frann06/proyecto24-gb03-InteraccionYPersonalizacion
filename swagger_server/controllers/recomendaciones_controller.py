import connexion
import six

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Recomendaciones_DA1 import Recomendaciones_DA

recomendaciones_da = Recomendaciones_DA()

def recomendaciones_get():  # noqa: E501
    """Obtener recomendaciones generales

    Genera recomendaciones de contenido generales.

    :rtype: List[Contenido]
    """
    return {"message": "Error al obtener recomendaciones generales"}, 500

def recomendaciones_id_usuario_get(id_usuario, num_recomendaciones=5):  # noqa: E501
    """Obtener recomendaciones personalizadas

    Obtiene recomendaciones personalizadas para un usuario concreto.

    :param id_usuario: ID del usuario
    :type id_usuario: int
    :param num_recomendaciones: Número de recomendaciones a devolver
    :type num_recomendaciones: int
    :rtype: List[Contenido]
    """
    try:
        recomendaciones, status_code = recomendaciones_da.recomendaciones_aleatorias(id_usuario, num_recomendaciones)
        return recomendaciones, status_code
    except Exception as e:
        print(f"Error en recomendaciones_id_usuario_get: {e}")
        return {"message": "Error al obtener recomendaciones personalizadas"}, 500