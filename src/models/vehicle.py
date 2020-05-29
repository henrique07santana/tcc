from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model

table_name = 'vehicle'

class Vehicle(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('vehicle_id_seq'), primary_key=True)
    vehicle_type_id = Column(Integer, ForeignKey('vehicle_type.id'))
    created_at = Column(DateTime)

    def __init__(self, vehicle_type_id:int):
        self.vehicle_type_id = vehicle_type_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Vehicle(vehicle_type_id='%s')>" % (self.vehicle_type_id)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
