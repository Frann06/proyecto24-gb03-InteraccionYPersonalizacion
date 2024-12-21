from swagger_server.database_setup import db, Display  # Asegúrate de que Display esté importado correctamente
from swagger_server.models.visualizacion import Visualizacion as DisplayModel  # Asumiendo que tienes un modelo Display
from sqlalchemy import desc  # Asegúrate de importar esto

class Displays_DA:
    # Clase para acceder a la tabla Display de la base de datos
    def __init__(self) -> None:
        pass

    def create_display(self, display: DisplayModel):
        # Crear una visualización
        displayDB = Display(
            id_perfil=display.id_perfil,
            id_contenido=display.id_contenido,
            fecha_visualizacion=display.fecha_visualizacion,
            progreso=display.progreso,
        )
        try:
            db.add(displayDB)
            db.commit()
            return displayDB
        except Exception as e:
            db.rollback()
            print(f"Error creando visualización: {e}")
            return None
    
    def get_display_by_id(self, id: int):
        # Obtener una visualización por ID
        try:
            display = db.query(Display).get(id)
            return display
        except Exception as e:
            print(f"Error obteniendo visualización por ID: {e}")
            return None
        
    def get_displays_by_perfil(self, id_perfil: int):
   
        try:
            # Filtrar por id_perfil y ordenar por fecha_visualizacion descendente
            displays = db.query(Display).filter(Display.id_perfil == id_perfil).order_by(desc(Display.fecha_visualizacion)).all()
            return displays
        except Exception as e:
            print(f"Error obteniendo visualizaciones por perfil: {e}")
            return None

    def get_all_displays(self):
        # Obtener todas las visualizaciones
        try:
            displays = db.query(Display).all()
            return displays
        except Exception as e:
            print(f"Error obteniendo todas las visualizaciones: {e}")
            return None
    
    def update_display(self, display: DisplayModel, id_visualizacion: int):
   
        try:
            # Filtrar la visualización por el id_visualizacion
            displayDB = db.query(Display).filter(Display.id_visualizacion == id_visualizacion).first()
            
            # Verificar que displayDB existe
            if displayDB is None:
                print(f"Visualización con id {id_visualizacion} no encontrada.")
                return None

            # Actualizar los campos de la visualización
            displayDB.id_perfil = display.id_perfil
            displayDB.id_contenido = display.id_contenido
            displayDB.fecha_visualizacion = display.fecha_visualizacion
            displayDB.progreso = display.progreso

            # Guardar los cambios
            db.commit()
            return displayDB
        except Exception as e:
            # Revertir en caso de error
            db.rollback()
            print(f"Error actualizando visualización: {e}")
            return None

    def delete_display(self, id_perfil: int):
        # Eliminar una visualización
        try:
            display = db.query(Display).filter(Display.id_perfil==id_perfil).first()
            db.delete(display)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error eliminando visualización: {e}")

    def delete_display_id_visualizacion(self, id_visualizacion: int):
        # Eliminar una visualización
        try:
            display = db.query(Display).filter(Display.id_visualizacion==id_visualizacion).first()
            db.delete(display)
            db.commit()
        except Exception as e:
            db.rollback()
            print(f"Error eliminando visualización: {e}")



    def get_visualizacion_by_contenido_y_perfil(self, id_contenido: int, id_perfil: int):
        """Obtener una visualización por id_contenido y id_perfil."""
        try:
            return db.query(Display).filter(
                Display.id_contenido == id_contenido,
                Display.id_perfil == id_perfil
            ).first()
        except Exception as e:
            print(f"Error al obtener visualización: {e}")
            return None
