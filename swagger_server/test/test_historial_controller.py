# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.visualizacion import Visualizacion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestHistorialController(BaseTestCase):
    """HistorialController integration test stubs"""

    def test_historial_get(self):
        """Test case for historial_get

        Obtener historial de visualizaciones
        """
        response = self.client.open(
            '/v1/historial',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_id_visualizacion_delete(self):
        """Test case for historial_id_visualizacion_delete

        Eliminar una entrada del historial
        """
        response = self.client.open(
            '/v1/historial/{id_visualizacion}'.format(id_visualizacion=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_id_visualizacion_get(self):
        """Test case for historial_id_visualizacion_get

        Obtener una entrada específica del historial
        """
        response = self.client.open(
            '/v1/historial/{id_visualizacion}'.format(id_visualizacion=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_id_visualizacion_put(self):
        """Test case for historial_id_visualizacion_put

        Actualizar una visualizacion del historial
        """
        body = Visualizacion()
        response = self.client.open(
            '/v1/historial/{id_visualizacion}'.format(id_visualizacion=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_perfil_id_perfil_delete(self):
        """Test case for historial_perfil_id_perfil_delete

        Eliminar todo el historial de un perfil
        """
        response = self.client.open(
            '/v1/historial/perfil/{id_perfil}'.format(id_perfil=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_perfil_id_perfil_get(self):
        """Test case for historial_perfil_id_perfil_get

        Obtener todas las entradas del historial de un perfil
        """
        response = self.client.open(
            '/v1/historial/perfil/{id_perfil}'.format(id_perfil=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_historial_post(self):
        """Test case for historial_post

        Agregar entrada al historial
        """
        body = Visualizacion()
        response = self.client.open(
            '/v1/historial',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
