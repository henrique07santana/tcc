from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.transit import Transit

table_name = 'boarding_gate'

class BoardingGate(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('boarding_gate_id_seq'), primary_key=True)
    number = Column(Integer)
    area = Column(String(50))
    terminal = Column(String(50))
    created_at = Column(DateTime)
    station_id = Column(Integer, ForeignKey('station.id'))
    transit = relationship(Transit, backref='boarding_gate')


    def __init__(self, number:int, station_id:int, area:str=None, terminal:str=None):
        self.number = number
        self.area = area
        self.terminal = terminal
        self.station_id = station_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<BoardingGate(number='%s', station_id='%s')>" % (self.number, self.station_id)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
