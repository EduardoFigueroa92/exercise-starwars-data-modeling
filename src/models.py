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
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    contraseña = Column(String)

    favoritos = relationship("Favoritos", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', apellido='{self.apellido}', email='{self.email}')>"




class Favoritos(Base):
    __tablename__ = 'favoritos'

    id = Column(Integer, primary_key=True)
    tipo = Column(String)  # Puede ser 'planeta' o 'personaje'
    favorito_id = Column(Integer)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    
    planeta = relationship("Planetas", foreign_keys=[favorito_id], backref="favoritos")
    personaje = relationship("Personajes", foreign_keys=[favorito_id], backref="favoritos")

    usuario = relationship("Usuario", back_populates="favoritos")


class Planetas(Base):
    __tablename__ = 'planetas'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    favoritos = relationship("Favoritos", backref="planetas")


class Personajes(Base):
    __tablename__ = 'personajes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)

    favoritos = relationship("Favoritos", backref="personajes")


Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    addresses = relationship("Address", back_populates="person")

    favoritos = relationship("Favoritos", backref="person")


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('Person.id'))

    person = relationship("Person", back_populates="addresses")

    def to_dict(self):
        return {
            "id": self.id,
            "street_name": self.street_name,
            "street_number": self.street_number,
            "post_code": self.post_code,
            "person_id": self.person_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
