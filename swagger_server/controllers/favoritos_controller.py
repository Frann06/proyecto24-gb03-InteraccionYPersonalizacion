import connexion
from swagger_server.models.favorito import Favorito  # Asegúrate de que el modelo Favorito esté importado correctamente
from swagger_server.database_setup import db
from swagger_server.data_access.Favorite_DA import Favorite_DA  # Asegúrate de que Favorite_DA esté correctamente importado

# Crear una instancia de la clase de acceso a datos para favoritos
favorite_dao = Favorite_DA()

def favoritos_get(id_perfil):  # noqa: E501
    """Obtener favoritos

    Recupera la lista de contenidos favoritos de un perfil.

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: List[Favorito]
    """
    try:
        # Obtener todos los favoritos del perfil
        favoritos = favorite_dao.get_favorites_by_perfil(id_perfil)
        return [favorito.to_dict() for favorito in favoritos] if favoritos else [], 200
    except Exception as e:
        print(f"Error al obtener los favoritos: {e}")
        return {"message": "Error al obtener los favoritos"}, 500


def favoritos_id_favorito_delete(id_favorito):  # noqa: E501
    """Eliminar un favorito

    Elimina un contenido de la lista de favoritos por su ID.

    :param id_favorito: ID del favorito
    :type id_favorito: int

    :rtype: None
    """
    try:
        favorite_dao.delete_favorite(id_favorito)
        return {"message": "Favorito eliminado exitosamente"}, 204
    except Exception as e:
        print(f"Error al eliminar el favorito: {e}")
        return {"message": "Error al eliminar el favorito"}, 500


def favoritos_post(body):  # noqa: E501
    """Agregar a favoritos

    Añade un contenido a la lista de favoritos de un perfil.

    :param body: 
    :type body: dict | bytes

    :rtype: Favorito
    """
    if connexion.request.is_json:
        body = Favorito.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Verificar si el favorito ya existe
        existing_favorite = favorite_dao.get_favorite_by_profile_and_content(body.id_perfil, body.id_contenido)
        if existing_favorite:
            return {"message": "El favorito ya existe."}, 400  # 400 Bad Request

        # Crear el favorito en la base de datos
        nuevo_favorito = favorite_dao.create_favorite(body)
        return nuevo_favorito.to_dict(), 201
    except Exception as e:
        print(f"Error al agregar a favoritos: {e}")
        return {"message": "Error al agregar a favoritos"}, 500

