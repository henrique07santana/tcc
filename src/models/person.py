from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.passenger import Passenger

table_name = 'person'

class Person(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    products = relationship(Passenger, backref="person")

    def __init__(self, name:str, email:str):
        self.name = name
        self.email = email
        self.table_name = table_name

    def __repr__(self):
        return "<Person(name='%s', email='%s')>" % (self.name, self.email)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
