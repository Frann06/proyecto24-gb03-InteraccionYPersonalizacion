import connexion
import six
from swagger_server.models.visualizacion import Visualizacion  # noqa: E501
from swagger_server import util
from swagger_server.database_setup import db
from swagger_server.models.visualizacion import Visualizacion as VisualizacionModel
from swagger_server.data_access.Displays_DA import Displays_DA  # Asegúrate de que la clase esté correctamente importada

visualizacion_dao = Displays_DA()

def historial_get():  # noqa: E501
    """Obtener historial de visualizaciones

    Recupera todas las entradas de historial creadas. # noqa: E501

    :rtype: List[Visualizacion]
    """
    try:
        historial = visualizacion_dao.get_all_displays()  # Obtener todas las visualizaciones
        return [visualizacion.to_dict() for visualizacion in historial], 200
    except Exception as e:
        print(f"Error al obtener historial: {e}")
        return {"message": "Error al obtener historial"}, 500

def historial_id_visualizacion_delete(id_visualizacion):  # noqa: E501
    """Eliminar una entrada del historial

    Elimina una visualización específica del historial por su ID. # noqa: E501

    :param id_visualizacion: ID único de la visualizacion
    :type id_visualizacion: int

    :rtype: None
    """
    try:
        visualizacion_dao.delete_display_id_visualizacion(id_visualizacion)
        return {"message": "Visualización eliminada correctamente."}, 204  # 204 No Content
    except Exception as e:
        print(f"Error al eliminar visualización: {e}")
        return {"message": "Error al eliminar visualización"}, 500

def historial_id_visualizacion_get(id_visualizacion):  # noqa: E501
    """Obtener una entrada específica del historial

    Recupera una entrada específica del historial por su ID. # noqa: E501

    :param id_visualizacion: ID único de la visualizacion
    :type id_visualizacion: int

    :rtype: Visualizacion
    """
    try:
        visualizacion = visualizacion_dao.get_display_by_id(id_visualizacion)
        if visualizacion:
            return visualizacion.to_dict(), 200
        else:
            return {"message": "Visualización no encontrada."}, 404  # 404 Not Found
    except Exception as e:
        print(f"Error al obtener visualización: {e}")
        return {"message": "Error al obtener visualización"}, 500

def historial_id_visualizacion_put(body, id_visualizacion):  # noqa: E501
    """
    Actualizar una visualización específica del historial usando id_visualizacion

    :param body: Información actualizada de la visualización en formato JSON
    :type body: dict | bytes
    :param id_visualizacion: ID único de la visualización
    :type id_visualizacion: int

    :rtype: dict
    """
    if connexion.request.is_json:
        # Convertimos el cuerpo de la solicitud a un objeto Visualizacion o DisplayModel
        body = Visualizacion.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Llamar al método update_display con el objeto de datos y el id_visualizacion
        updated_visualizacion = visualizacion_dao.update_display(body, id_visualizacion)
        
        # Verificar si la visualización existe
        if updated_visualizacion is None:
            return {"message": "Visualización no encontrada"}, 404

        # Retornar la visualización actualizada en formato dict y el código 200
        return updated_visualizacion.to_dict(), 200
    except Exception as e:
        # En caso de error, devolver mensaje y código 500
        print(f"Error al actualizar visualización: {e}")
        return {"message": "Error al actualizar visualización"}, 500


def historial_perfil_id_perfil_delete(id_perfil):  # noqa: E501
    """Eliminar todo el historial de un perfil

    Elimina todas las entradas de historial asociadas a un perfil específico. # noqa: E501

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: None
    """
    try:
        visualizacion_dao.delete_display(id_perfil)
        return {"message": "Historial eliminado correctamente."}, 204  # 204 No Content
    except Exception as e:
        print(f"Error al eliminar historial del perfil: {e}")
        return {"message": "Error al eliminar historial"}, 500

def historial_perfil_id_perfil_get(id_perfil):  # noqa: E501
    """Obtener todas las entradas del historial de un perfil

    Recupera todas las entradas de visualizaciones asociadas a un perfil específico. # noqa: E501

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: List[Visualizacion]
    """
    try:
        historial = visualizacion_dao.get_displays_by_perfil(id_perfil)
        return [visualizacion.to_dict() for visualizacion in historial], 200
    except Exception as e:
        print(f"Error al obtener historial del perfil: {e}")
        return {"message": "Error al obtener historial"}, 500

def historial_post(body):  # noqa: E501
    """Agregar entrada al historial

    Añade una nueva entrada de una visualización al historial de visualizaciones. 
    Si ya existe una entrada con el mismo id_contenido e id_perfil, se elimina la existente antes de agregar la nueva.

    :param body: 
    :type body: dict | bytes

    :rtype: Visualizacion
    """
    if connexion.request.is_json:
        body = Visualizacion.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        # Primero, verificar si ya existe una visualización con el mismo id_contenido e id_perfil
        existing_visualizacion = visualizacion_dao.get_visualizacion_by_contenido_y_perfil(
            id_contenido=body.id_contenido,
            id_perfil=body.id_perfil
        )

        # Si existe, eliminar la entrada existente
        if existing_visualizacion:
            visualizacion_dao.delete_display_id_visualizacion(existing_visualizacion.id_visualizacion)

        # Crear la nueva visualización en el historial
        nuevo_historial = visualizacion_dao.create_display(body)
        return nuevo_historial.to_dict(), 201  # 201 Created

    except Exception as e:
        print(f"Error al agregar entrada al historial: {e}")
        return {"message": "Error al agregar entrada al historial"}, 500

