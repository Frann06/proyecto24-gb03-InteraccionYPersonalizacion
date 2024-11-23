import connexion
import six

from swagger_server.models.favorito import Favorito  # noqa: E501
from swagger_server import util


def favoritos_get(id_perfil):  # noqa: E501
    """Obtener favoritos

    Recupera la lista de contenidos favoritos de un perfil. # noqa: E501

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: List[Favorito]
    """
    return 'do some magic!'


def favoritos_id_favorito_delete(id_favorito):  # noqa: E501
    """Eliminar un favorito

    Elimina un contenido de la lista de favoritos por su ID. # noqa: E501

    :param id_favorito: ID del favorito
    :type id_favorito: int

    :rtype: None
    """
    return 'do some magic!'


def favoritos_post(body):  # noqa: E501
    """Agregar a favoritos

    Añade un contenido a la lista de favoritos de un perfil. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Favorito
    """
    if connexion.request.is_json:
        body = Favorito.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
