from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model

table_name = 'transit'

class Transit(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('transit_id_seq'), primary_key=True)
    boarding_time = Column(DateTime)
    boarding_gate_id = Column(Integer, ForeignKey('boarding_gate.id'))
    route_id = Column(Integer, ForeignKey('route.id'))
    span_id = Column(Integer, ForeignKey('span.id'))
    vehicle_type_id = Column(Integer, ForeignKey('vehicle_type.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    created_at = Column(DateTime)

    def __init__(self, boarding_time:datetime, route_id:int, span_id:int, vehicle_type_id:int, vehicle_id:int=None, boarding_gate_id:int=None):
        self.boarding_time = boarding_time
        self.route_id = route_id
        self.boarding_gate_id = boarding_gate_id
        self.route_id = route_id
        self.span_id = span_id
        self.vehicle_id = vehicle_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Transit(boarding_time='%s', span_id='%s')>" % (self.boarding_time, self.span_id)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
