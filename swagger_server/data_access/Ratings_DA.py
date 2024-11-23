from swagger_server.database_setup import db, Rating  # Asegúrate de que Rating esté importado correctamente
from swagger_server.models.rating import Rating as RatingModel  # Asumiendo que tienes un modelo Rating

class Ratings_DA:
    def __init__(self) -> None:
        pass

    def create_rating(self, rating: RatingModel):
        # Crear un rating
        ratingDB = Rating(
            id_contenido=rating.id_contenido,
            id_perfil=rating.id_perfil,
            thumb_up=rating.thumb_up,
        )
        try:
            db.add(ratingDB)
            db.commit()
            return ratingDB
        except Exception as e:
            db.rollback()
            print(f"Error creando rating: {e}")
            return None
    
    def get_rating_by_id(self, id: int):
        # Obtener un rating por ID
        try:
            rating = db.query(Rating).get(id)
            return rating
        except Exception as e:
            print(f"Error obteniendo rating por ID: {e}")
            return None
        
    def get_ratings_by_perfil(self, id_perfil: int):
        # Obtener todos los ratings de un perfil
        try:
            ratings = db.query(Rating).filter(Rating.id_perfil == id_perfil).all()
            return ratings
        except Exception as e:
            print(f"Error obteniendo ratings por perfil: {e}")
            return None

    def get_all_ratings(self):
        # Obtener todos los ratings
        try:
            ratings = db.query(Rating).all()
            return ratings
        except Exception as e:
            print(f"Error obteniendo todos los ratings: {e}")
            return None
    
    def update_rating(self, rating: RatingModel, id_rating: int):
    
        try:
            # Filtrar el rating por id_rating
            ratingDB = db.query(Rating).get(id_rating)
            
            # Verificar que ratingDB existe
            if ratingDB is None:
                print(f"Rating con id {id_rating} no encontrado.")
                return None

            # Actualizar los campos del rating
            ratingDB.id_contenido = rating.id_contenido
            ratingDB.id_perfil = rating.id_perfil
            ratingDB.thumb_up = rating.thumb_up

            # Guardar los cambios
            db.commit()
            return ratingDB
        except Exception as e:
            # Revertir en caso de error
            db.rollback()
            print(f"Error actualizando rating: {e}")
            return None


    def delete_rating(self, id: int):
        # Eliminar un rating
        try:
            rating = db.query(Rating).get(id)
            db.delete(rating)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error eliminando rating: {e}")


    def get_rating_by_contenido_y_perfil(self, id_contenido: int, id_perfil: int):
        """Obtener un rating por id_contenido y id_perfil."""
        try:
            return db.query(Rating).filter(
                Rating.id_contenido == id_contenido,
                Rating.id_perfil == id_perfil
            ).first()
        except Exception as e:
            print(f"Error al obtener rating: {e}")
            return None
        

    def get_ratings_by_contenido(self, id_contenido: int):
        """Obtener todos los ratings de un contenido específico.

        :param id_contenido: ID del contenido para el cual se desean obtener los ratings
        :type id_contenido: int

        :rtype: List[Rating] | None
        """
        try:
            ratings = db.query(Rating).filter(Rating.id_contenido == id_contenido).all()
            return ratings
        except Exception as e:
            print(f"Error obteniendo ratings por contenido: {e}")
            return None