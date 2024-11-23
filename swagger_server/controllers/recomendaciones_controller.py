import connexion
import six

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server import util


def recomendaciones_get():  # noqa: E501
    """Obtener recomendaciones generales

    Genera recomendaciones de contenido generales # noqa: E501


    :rtype: List[Contenido]
    """
    return 'do some magic!'


def recomendaciones_id_usuario_get(id_usuario):  # noqa: E501
    """Obtener recomendaciones personalizadas

    Obtiene recomendaciones personalizadas para un usuario concreto # noqa: E501

    :param id_usuario: ID del usuario
    :type id_usuario: int

    :rtype: List[Contenido]
    """
    return 'do some magic!'
