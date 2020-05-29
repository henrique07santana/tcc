from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.ticket import Ticket

table_name = 'seat'

class Seat(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('seat_id_seq'), primary_key=True)
    name = Column(String(50))
    number = Column(Integer)
    vehicle_type_id = Column(Integer, ForeignKey('vehicle_type.id'))
    transit = relationship(Ticket, backref='seat')
    created_at = Column(DateTime)

    def __init__(self, name:str, number:int, vehicle_type_id:int):
        self.name = name
        self.number = number
        self.vehicle_type_id = vehicle_type_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Seat(name='%s', number='%s')>" % (self.name, self.number)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
