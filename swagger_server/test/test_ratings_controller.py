# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.rating import Rating  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRatingsController(BaseTestCase):
    """RatingsController integration test stubs"""

    def test_ratings_content_id_contenido_get(self):
        """Test case for ratings_content_id_contenido_get

        Obtener ratings por contenido
        """
        response = self.client.open(
            '/v1/ratings/content/{id_contenido}'.format(id_contenido=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ratings_id_rating_delete(self):
        """Test case for ratings_id_rating_delete

        Eliminar un rating
        """
        response = self.client.open(
            '/v1/ratings/{id_rating}'.format(id_rating=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ratings_id_rating_get(self):
        """Test case for ratings_id_rating_get

        Obtener un rating específico
        """
        response = self.client.open(
            '/v1/ratings/{id_rating}'.format(id_rating=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ratings_id_rating_put(self):
        """Test case for ratings_id_rating_put

        Actualizar un rating
        """
        body = Rating()
        response = self.client.open(
            '/v1/ratings/{id_rating}'.format(id_rating=56),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ratings_post(self):
        """Test case for ratings_post

        Crear un rating
        """
        body = Rating()
        response = self.client.open(
            '/v1/ratings',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
