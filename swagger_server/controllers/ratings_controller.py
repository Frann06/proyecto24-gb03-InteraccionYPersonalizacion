import connexion
import six

from swagger_server.models.rating import Rating  # noqa: E501
from swagger_server import util
from swagger_server.database_setup import Rating as RatingModel  # Importa el modelo Rating
from swagger_server.data_access.Ratings_DA import Ratings_DA  # Importa la clase Rating_DA

rating_dao = Ratings_DA()  # Instancia de la clase Rating_DA

def ratings_content_id_contenido_get(id_contenido):  # noqa: E501
    """Obtener ratings por contenido

    Recupera todos los ratings asociados a un contenido específico mediante su ID.

    :param id_contenido: ID del contenido para el cual se desean obtener los ratings
    :type id_contenido: int

    :rtype: List[Rating]
    """
    try:
        ratings = rating_dao.get_ratings_by_contenido(id_contenido)
        return [rating.to_dict() for rating in ratings], 200  # 200 OK
    except Exception as e:
        print(f"Error al obtener ratings: {e}")
        return {"message": "Error al obtener ratings"}, 500

def ratings_id_rating_delete(id_rating):  # noqa: E501
    """Eliminar un rating

    Elimina un rating por su ID.

    :param id_rating: ID del rating
    :type id_rating: int

    :rtype: None
    """
    try:
        rating_dao.delete_rating(id_rating)
        return {"message": "Rating eliminado exitosamente"}, 204  # 204 No Content
    except Exception as e:
        print(f"Error al eliminar rating: {e}")
        return {"message": "Error al eliminar rating"}, 500

def ratings_id_rating_get(id_rating):  # noqa: E501
    """Obtener un rating específico

    Recupera un rating por su ID.

    :param id_rating: ID del rating
    :type id_rating: int

    :rtype: Rating
    """
    try:
        rating = rating_dao.get_rating_by_id(id_rating)
        if rating is None:
            return {"message": "Rating no encontrado"}, 404  # 404 Not Found
        return rating.to_dict(), 200  # 200 OK
    except Exception as e:
        print(f"Error al obtener rating: {e}")
        return {"message": "Error al obtener rating"}, 500

def ratings_id_rating_put(body, id_rating):  # noqa: E501
    """
    Actualizar un rating existente usando su id_rating

    :param body: Información actualizada del rating en formato JSON
    :type body: dict | bytes
    :param id_rating: ID único del rating
    :type id_rating: int

    :rtype: dict
    """
    if connexion.request.is_json:
        # Convertimos el cuerpo de la solicitud a un objeto Rating
        body = Rating.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Verificar si el rating existe antes de intentar actualizar
        existing_rating = rating_dao.get_rating_by_id(id_rating)
        if existing_rating is None:
            return {"message": "Rating no encontrado"}, 404  # 404 Not Found

        # Llamar al método update_rating con el objeto de datos y el id_rating
        updated_rating = rating_dao.update_rating(body, id_rating)
        
        # Verificar si la actualización fue exitosa
        if updated_rating is None:
            return {"message": "Error al actualizar rating"}, 500

        # Retornar el rating actualizado en formato dict y el código 200
        return updated_rating.to_dict(), 200  # 200 OK
    except Exception as e:
        # En caso de error, devolver mensaje y código 500
        print(f"Error al actualizar rating: {e}")
        return {"message": "Error al actualizar rating"}, 500


def ratings_post(body):  # noqa: E501
    """Crear un rating

    Crea un nuevo rating para un contenido por un perfil.

    :param body: 
    :type body: dict | bytes

    :rtype: Rating
    """
    if connexion.request.is_json:
        body = Rating.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Verificar si ya existe un rating con el mismo id_contenido e id_perfil
        existing_rating = rating_dao.get_rating_by_contenido_y_perfil(
            id_contenido=body.id_contenido,
            id_perfil=body.id_perfil
        )

        # Si existe, eliminar la entrada existente
        if existing_rating:
            rating_dao.delete_rating(existing_rating.id_rating)

        # Crear el nuevo rating
        nuevo_rating = rating_dao.create_rating(body)
        return nuevo_rating.to_dict(), 201  # 201 Created

    except Exception as e:
        print(f"Error al crear rating: {e}")
        return {"message": "Error al crear rating"}, 500
