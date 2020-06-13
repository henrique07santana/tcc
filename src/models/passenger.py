from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.ticket import Ticket

table_name = 'passenger'

class Passenger(Base):
    __tablename__ = table_name
    id = Column(Integer, Sequence('passenger_id_seq'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    phone_number = Column(String(50))
    created_at = Column(DateTime)
    ticket = relationship(Ticket, backref='passenger')

    def __init__(self, person_id:id, phone_number:str):
        self.person_id = person_id
        self.phone_number = phone_number
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Passenger(person_id='%s')>" % (self.person_id)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
