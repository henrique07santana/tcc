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

table_name = 'route'

class Route(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('route_id_seq'), primary_key=True)
    first_origin = Column(Integer, ForeignKey('station.id'))
    last_destination = Column(Integer, ForeignKey('station.id'))
    booking_id = Column(Integer, ForeignKey('booking.id'))
    created_at = Column(DateTime)
    transit = relationship(Transit, backref='route')

    def __init__(self, first_origin:int, last_destination:int, booking_id:int):
        self.first_origin = first_origin
        self.last_destination = last_destination
        self.booking_id = booking_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Route(first_origin='%s', last_destination='%s', booking_id='%s')>" % (self.first_origin, self.last_destination, self.booking_id)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
