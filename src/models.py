import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    climate = Column(String(20))
    terrain = Column(String(20))
    diameter = Column(String(20))
    rotation_period = Column(String(10))
    orbital_period = Column(String(10))
    gravity = Column(String(10))
    population = Column(String(20))

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(10))
    home_world_id = Column(Integer, ForeignKey('Planets.id'))
    home_world = relationship(Planet)

class Vehicle(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    manufacturer = Column(String(20))

class VehiclePilot(Base):
    __tablename__ = 'VehiclePilots'
    id = Column(Integer, primary_key=True)
    pilot_id = Column(Integer, ForeignKey('Characters.id'), nullable=False)
    pilot = relationship(Character)
    vehicle_id = Column(Integer, ForeignKey('Vehicles.id'), nullable=False)
    vehicle = relationship(Vehicle)

class FavoriteVehicle(Base):
    __tablename__ = 'FavoriteVehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('Vehicles.id'), unique=True, nullable=False)
    vehicle = relationship(Vehicle)

class FavoriteCharacter(Base):
    __tablename__ = 'FavoriteCharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('Characters.id'), unique=True, nullable=False)
    character = relationship(Character)

class FavoritePlanet(Base):
    __tablename__ = 'FavoritePlanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('Planets.id'), unique=True, nullable=False)
    planet = relationship(Planet)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
