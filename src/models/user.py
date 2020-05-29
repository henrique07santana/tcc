from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.booking import Booking

table_name = 'user'

class User(Base):
    __tablename__ = table_name
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    email = Column(String(50))
    password = Column(String(50))
    created_at = Column(DateTime)
    booking = relationship(Booking, backref='user')

    def __init__(self, person_id:id, email:str, password:str):
        self.person_id = person_id
        self.email = email
        self.password = password
        self.created_at = datetime.now()

    def __repr__(self):
        return "<User(email='%s')>" % (self.email)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
