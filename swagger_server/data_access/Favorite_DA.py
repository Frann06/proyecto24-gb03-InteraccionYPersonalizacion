from swagger_server.database_setup import db, Favorite  # Asegúrate de que Favorite esté importado correctamente
from swagger_server.models.favorito import Favorito as FavoriteModel  # Asumiendo que tienes un modelo Favorite

class Favorite_DA:
    def __init__(self) -> None:
        pass

    def create_favorite(self, favorite: FavoriteModel):
        # Crear un favorite
        favoriteDB = Favorite(
            id_perfil=favorite.id_perfil,
            id_contenido=favorite.id_contenido,
            fecha_agregado=favorite.fecha_agregado,
        )
        try:
            db.add(favoriteDB)
            db.commit()
            return favoriteDB
        except Exception as e:
            db.rollback()
            print(f"Error creando favorito: {e}")
            return None
    
    def get_favorite_by_id(self, id: int):
        # Obtener un favorite por ID
        try:
            favorite = db.query(Favorite).get(id)
            return favorite
        except Exception as e:
            print(f"Error obteniendo favorito por ID: {e}")
            return None
        
    def get_favorites_by_perfil(self, id_perfil: int):
        # Obtener todos los favorites de un perfil
        try:
            favorites = db.query(Favorite).filter(Favorite.id_perfil == id_perfil).all()
            return favorites
        except Exception as e:
            print(f"Error obteniendo favoritos por perfil: {e}")
            return None

    def get_all_favorites(self):
        # Obtener todos los favorites
        try:
            favorites = db.query(Favorite).all()
            return favorites
        except Exception as e:
            print(f"Error obteniendo todos los favoritos: {e}")
            return None
    
    def update_favorite(self, favorite: FavoriteModel):
        # Actualizar un favorite
        try:
            favoriteDB = db.query(Favorite).get(favorite.id_favorito)
            favoriteDB.id_perfil = favorite.id_perfil
            favoriteDB.id_contenido = favorite.id_contenido
            favoriteDB.fecha_agregado = favorite.fecha_agregado
            db.commit()
            return favoriteDB
        except Exception as e:
            db.rollback()
            print(f"Error actualizando favorito: {e}")
            return None

    def delete_favorite(self, id: int):
        # Eliminar un favorite
        try:
            favorite = db.query(Favorite).get(id)
            db.delete(favorite)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error eliminando favorito: {e}")

    def get_favorite_by_profile_and_content(self, id_perfil: int, id_contenido: int):
        """Verifica si existe un favorito para un perfil y contenido específicos.

        :param id_perfil: ID del perfil
        :param id_contenido: ID del contenido
        :type id_perfil: int
        :type id_contenido: int
        :rtype: Favorito or None
        """
        try:
            return db.query(Favorite).filter(
                Favorite.id_perfil == id_perfil,
                Favorite.id_contenido == id_contenido
            ).first()
        except Exception as e:
            print(f"Error al buscar el favorito: {e}")
            return None

