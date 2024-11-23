# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRecomendacionesController(BaseTestCase):
    """RecomendacionesController integration test stubs"""

    def test_recomendaciones_get(self):
        """Test case for recomendaciones_get

        Obtener recomendaciones generales
        """
        response = self.client.open(
            '/v1/recomendaciones',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recomendaciones_id_usuario_get(self):
        """Test case for recomendaciones_id_usuario_get

        Obtener recomendaciones personalizadas
        """
        response = self.client.open(
            '/v1/recomendaciones/{id_usuario}'.format(id_usuario=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
