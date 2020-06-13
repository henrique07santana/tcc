from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.passenger import Passenger
from models.user import User

table_name = 'person'

class Person(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50))
    document = Column(String(50))
    passenger = relationship(Passenger, backref='person')
    user = relationship(User, backref='person')
    created_at = Column(DateTime)

    def __init__(self, name:str, document:str):
        self.name = name
        self.document = document
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Person(name='%s', document='%s')>" % (self.name, self.document)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
        