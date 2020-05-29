from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.vehicle import Vehicle
from models.transit import Transit

table_name = 'vehicle_type'

class VehicleType(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('vehicle_type_id_seq'), primary_key=True)
    name = Column(String(50))
    brand = Column(String(50))
    model = Column(String(50))
    capacity = Column(Integer)
    columns = Column(Integer)
    seats_per_column = Column(Integer)
    category = Column(String(50))
    vehicle = relationship(Vehicle, backref='vehicle_type')
    transit = relationship(Transit, backref='vehicle_type')
    created_at = Column(DateTime)

    def __init__(self, name:str, brand:str, model:str, capacity:int, columns:int, seats_per_column:int, category:str=None):
        self.name = name
        self.brand = brand
        self.model = model
        self.capacity = capacity
        self.columns = columns
        self.seats_per_column = seats_per_column
        self.category = category
        self.created_at = datetime.now()

    def __repr__(self):
        return "<VehicleType(capacity='%s')>" % (self.capacity)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
