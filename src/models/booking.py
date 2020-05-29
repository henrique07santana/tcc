from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.route import Route
from models.ticket import Ticket

table_name = 'booking'

class Booking(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('booking_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    price = Column(Integer)
    created_at = Column(DateTime)
    route = relationship(Route, backref='booking')
    ticket = relationship(Ticket, backref='booking')

    def __init__(self, user_id:int, price:int=None):
        self.user_id = user_id
        self.price = price
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Booking(user_id='%s', price='%s', created_at='%s')>" % (self.user_id, self.price, self.created_at)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
