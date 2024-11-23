import connexion
import six

from swagger_server.models.visualizacion import Visualizacion  # noqa: E501
from swagger_server import util


def historial_get():  # noqa: E501
    """Obtener historial de visualizaciones

    Recupera todas las entradas de historial creadas. # noqa: E501


    :rtype: List[Visualizacion]
    """
    return 'do some magic!'


def historial_id_visualizacion_delete(id_visualizacion):  # noqa: E501
    """Eliminar una entrada del historial

    Elimina una visualización específica del historial por su ID. # noqa: E501

    :param id_visualizacion: ID único de la visualizacion
    :type id_visualizacion: int

    :rtype: None
    """
    return 'do some magic!'


def historial_id_visualizacion_get(id_visualizacion):  # noqa: E501
    """Obtener una entrada específica del historial

    Recupera una entrada específica del historial por su ID. # noqa: E501

    :param id_visualizacion: ID único de la visualizacion
    :type id_visualizacion: int

    :rtype: Visualizacion
    """
    return 'do some magic!'


def historial_id_visualizacion_put(body, id_visualizacion):  # noqa: E501
    """Actualizar una visualizacion del historial

    Actualiza la información de una visualizacion específica del historial. # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id_visualizacion: ID único de la visualizacion
    :type id_visualizacion: int

    :rtype: Visualizacion
    """
    if connexion.request.is_json:
        body = Visualizacion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def historial_perfil_id_perfil_delete(id_perfil):  # noqa: E501
    """Eliminar todo el historial de un perfil

    Elimina todas las entradas de historial asociadas a un perfil específico. # noqa: E501

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: None
    """
    return 'do some magic!'


def historial_perfil_id_perfil_get(id_perfil):  # noqa: E501
    """Obtener todas las entradas del historial de un perfil

    Recupera todas las entradas de visualizaciones asociadas a un perfil específico. # noqa: E501

    :param id_perfil: ID del perfil del usuario
    :type id_perfil: int

    :rtype: List[Visualizacion]
    """
    return 'do some magic!'


def historial_post(body):  # noqa: E501
    """Agregar entrada al historial

    Añade una nueva entrada de una visualización al historial de visualizaciones. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Visualizacion
    """
    if connexion.request.is_json:
        body = Visualizacion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
