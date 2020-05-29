from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model

table_name = 'ticket'

class Ticket(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('ticket_id_seq'), primary_key=True)
    transit_id = Column(Integer, ForeignKey('transit.id'))
    price = Column(Integer)
    seat_id = Column(Integer, ForeignKey('seat.id'))
    passenger_id = Column(Integer, ForeignKey('passenger.id'))
    booking_id = Column(Integer, ForeignKey('booking.id'))
    created_at = Column(DateTime)

    def __init__(self, transit_id:int, price:int, seat_id:int, passenger_id:int, booking_id:int):
        self.transit_id = transit_id
        self.price = price
        self.seat_id = seat_id
        self.passenger_id = passenger_id
        self.booking_id = booking_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Ticket(transit_id='%s', price='%s')>" % (self.transit_id, self.price)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
