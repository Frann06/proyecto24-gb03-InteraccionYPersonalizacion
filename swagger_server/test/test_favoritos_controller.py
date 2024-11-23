# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.favorito import Favorito  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFavoritosController(BaseTestCase):
    """FavoritosController integration test stubs"""

    def test_favoritos_get(self):
        """Test case for favoritos_get

        Obtener favoritos
        """
        query_string = [('id_perfil', 56)]
        response = self.client.open(
            '/v1/favoritos',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_favoritos_id_favorito_delete(self):
        """Test case for favoritos_id_favorito_delete

        Eliminar un favorito
        """
        response = self.client.open(
            '/v1/favoritos/{id_favorito}'.format(id_favorito=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_favoritos_post(self):
        """Test case for favoritos_post

        Agregar a favoritos
        """
        body = Favorito()
        response = self.client.open(
            '/v1/favoritos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
