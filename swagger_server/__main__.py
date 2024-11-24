#!/usr/bin/env python3

import connexion
from swagger_server.database_setup import Base, engine
from swagger_server import encoder


def main():
    Base.metadata.create_all(engine)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API de Interacción y Personalización'}, pythonic_params=True)
    # Con el debug activado cada vez que hay un cambio se recarga, cuidado con archivos que se modifiquen
    app.run(port=8082, debug=True)


if __name__ == '__main__':
    main()
