import connexion
import six

from swagger_server.models.rating import Rating  # noqa: E501
from swagger_server import util


def ratings_content_id_contenido_get(id_contenido):  # noqa: E501
    """Obtener ratings por contenido

    Recupera todos los ratings asociados a un contenido específico mediante su ID. # noqa: E501

    :param id_contenido: ID del contenido para el cual se desean obtener los ratings
    :type id_contenido: int

    :rtype: List[Rating]
    """
    return 'do some magic!'


def ratings_id_rating_delete(id_rating):  # noqa: E501
    """Eliminar un rating

    Elimina un rating por su ID. # noqa: E501

    :param id_rating: ID del rating
    :type id_rating: int

    :rtype: None
    """
    return 'do some magic!'


def ratings_id_rating_get(id_rating):  # noqa: E501
    """Obtener un rating específico

    Recupera un rating por su ID. # noqa: E501

    :param id_rating: ID del rating
    :type id_rating: int

    :rtype: Rating
    """
    return 'do some magic!'


def ratings_id_rating_put(body, id_rating):  # noqa: E501
    """Actualizar un rating

    Actualiza un rating existente. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id_rating: ID del rating
    :type id_rating: int

    :rtype: Rating
    """
    if connexion.request.is_json:
        body = Rating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ratings_post(body):  # noqa: E501
    """Crear un rating

    Crea un nuevo rating para un contenido por un perfil. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Rating
    """
    if connexion.request.is_json:
        body = Rating.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
