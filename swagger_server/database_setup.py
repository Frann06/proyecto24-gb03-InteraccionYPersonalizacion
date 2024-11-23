from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import class_mapper

# Crear una clase base para las tablas
Base = declarative_base()

class Favorite(Base):
    __tablename__ = 'favorites'

    id_favorito = Column(Integer, primary_key=True, autoincrement=True)
    id_perfil = Column(Integer, nullable=False)  # Se puede agregar una relación con Profile si es necesario
    id_contenido = Column(Integer, nullable=False)  # Se puede agregar una relación con Content si es necesario
    fecha_agregado = Column(DateTime, nullable=False)

    # Si decides implementar relaciones, puedes hacerlo así:
    # perfil = relationship('Profile', back_populates='favorites')
    # contenido = relationship('Content', back_populates='favorites')

    def to_dict(self, include_relations=False):
        """
        Convierte la instancia del modelo a un diccionario.

        :param include_relations: Si es True, incluye las relaciones (si las hay).
        :return: Diccionario con los datos del favorito.
        """
        favorite_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }

        #if include_relations:
            # Incluir relaciones si existen
            # favorite_dict['perfil'] = self.perfil.to_dict() if self.perfil else None
            # favorite_dict['contenido'] = self.contenido.to_dict() if self.contenido else None

        return favorite_dict

class Rating(Base):
    __tablename__ = 'ratings'

    id_rating = Column(Integer, primary_key=True, autoincrement=True)
    id_contenido = Column(Integer, nullable=False)  # Se puede agregar una relación con Content si es necesario
    id_perfil = Column(Integer, nullable=False)  # Se puede agregar una relación con Profile si es necesario
    thumb_up = Column(Boolean, nullable=False)

    def to_dict(self, include_relations=False):
        """
        Convierte la instancia del modelo a un diccionario.

        :param include_relations: Si es True, incluye las relaciones (si las hay).
        :return: Diccionario con los datos del rating.
        """
        rating_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }

        #if include_relations:
            # Incluir relaciones si existen
            # rating_dict['contenido'] = self.contenido.to_dict() if self.contenido else None
            # rating_dict['perfil'] = self.perfil.to_dict() if self.perfil else None

        return rating_dict
    

class Display(Base):
    __tablename__ = 'displays'

    id_visualizacion = Column(Integer, primary_key=True, autoincrement=True)
    id_perfil = Column(Integer, nullable=False)  # Se puede agregar una relación con Profile si es necesario
    id_contenido = Column(Integer, nullable=False)  # Se puede agregar una relación con Content si es necesario
    fecha_visualizacion = Column(DateTime, nullable=False)
    progreso = Column(Float, nullable=False)

    def to_dict(self, include_relations=False):
        """
        Convierte la instancia del modelo a un diccionario.

        :param include_relations: Si es True, incluye las relaciones (si las hay).
        :return: Diccionario con los datos de la visualización.
        """
        display_dict = {
            column.key: getattr(self, column.key)
            for column in class_mapper(self.__class__).columns
        }

        #if include_relations:
            # Incluir relaciones si existen
            # display_dict['perfil'] = self.perfil.to_dict() if self.perfil else None
            # display_dict['contenido'] = self.contenido.to_dict() if self.contenido else None

        return display_dict

# Crear el motor de base de datos usando SQLite (el archivo se llamará 'mydatabase.db')
engine = create_engine('sqlite:///database.db')


# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
db = Session()
