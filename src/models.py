from datetime import date
import os
from typing import List
from sqlalchemy import create_engine, String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class Films(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))
    episode_id: Mapped[int] = mapped_column(Integer)
    director: Mapped[str] = mapped_column(String(50))
    producer: Mapped[str] = mapped_column(String(50))
    release_date: Mapped[str] = mapped_column(String(50))

    def __repr__(self):
        return "<Films {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }

class Planets(Base):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[str] = mapped_column(String(50))
    gravity:Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))

    inhabitans: Mapped[List["People"]] = relationship('People')

    def __repr__(self):
        return f"<Planets(id: {self.id!r}, name: {self.name!r}, diameter: {self.diameter!r}, gravity: {self.gravity!r}, population: {self.population!r})>"

    def serialize(self):
        return {
            "id": self.id
        }


class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    height: Mapped[int] = mapped_column(Integer)
    mass: Mapped[int] = mapped_column(Integer)
    birth_year : Mapped[str] = mapped_column(String(10))
    gender : Mapped[str] = mapped_column(String(10))
    homeworld: Mapped[str] = mapped_column(ForeignKey('planets.id'))

    planet: Mapped["Planets"] = relationship('Planets', back_populates='')


    def __repr__(self):
        return f"<People:(id: {self.id!r}, name: {self.name!r}, birth year: {self.birth_year!r}, gender: {self.gender!r})>"

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "home_world": self.homeworld
        }


class Locations(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    film_id: Mapped[int] = mapped_column(ForeignKey('films.id'))
    planet_id: Mapped[int] = mapped_column(ForeignKey('planets.id'))


    def __repr__(self):
        return "<Location {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }


class Character(Base):
    __tablename__ = "charaters"
    id: Mapped[int] = mapped_column(primary_key=True)
    film_id:Mapped[int] = mapped_column(ForeignKey('films.id'))
    people_id:Mapped[int] = mapped_column(ForeignKey('people.id'))
    
    def __repr__(self):
        return "<Character {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }

#--------------------------------------------------------------------
# Don't edit the lines bellow here - No edite la lineas abajo de aquí
#--------------------------------------------------------------------
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    db_url = db_url.replace("postgres://", "postgresql://")
else:
    db_url = "sqlite:////tmp/test.db"


# You can add 'echo=True' as param to the next line and see the sql under the hood
# You can add 'echo=True' as param to the next line and see the sql under the hood
engine = create_engine(db_url, echo=True)

Session = sessionmaker(bind=engine)
db = Session()
