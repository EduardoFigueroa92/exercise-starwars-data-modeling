import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    fecha_creacion = Column(String)

    FavoritosPersonaje = relationship("FavoritosPersonaje", backref="usuario", lazy=True)
    FavoritosPlaneta = relationship("FavoritosPlaneta", backref="usuario", lazy=True)
    FavoritosVehiculo = relationship("FavoritosVehiculo", backref="usuario", lazy=True)
    
class FavoritosPersonaje(Base):
    __tablename__ = 'favoritosPersonaje'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))

class FavoritosPlaneta(Base):
    __tablename__ = 'favoritosPlaneta'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'))


class FavoritosVehiculo(Base):
    __tablename__ = 'favoritosVehiculo'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    vehiculo_id = Column(Integer, ForeignKey('vehiculo.id'))


class Planeta(Base):
    __tablename__ = 'planetas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    clima = Column(String)
    terreno = Column(String)
    poblacion = Column(Integer)

    FavoritosPlaneta = relationship("FavoritosPlaneta", backref="planeta", lazy=True)


class Personaje(Base):
    __tablename__ = 'personaje'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especie = Column(String)
    altura = Column(Integer)
    peso = Column(Integer)

    FavoritosPersonaje = relationship("FavoritosPersonaje", backref="personajes", lazy=True)


class Vehiculo(Base):
    __tablename__ = 'vehiculo'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    especie = Column(String)
    altura = Column(Integer)
    peso = Column(Integer)

    FavoritosVehiculo = relationship("FavoritosVehiculo", backref="vehiculos", lazy=True)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
