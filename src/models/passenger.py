from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base

table_name = 'passenger'

class Passenger(Base):
    __tablename__ = table_name
    id = Column(Integer, Sequence('passenger_id_seq'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    document = Column(String(50))

    def __init__(self, person_id:id, document:str):
        self.person_id = person_id
        self.document = document
        self.table_name = table_name

    def __repr__(self):
        return "<Passenger(document='%s')>" % (self.document)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
