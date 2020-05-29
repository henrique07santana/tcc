from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model

table_name = 'span'

class Span(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('span_id_seq'), primary_key=True)
    name = Column(String(50))
    origin_id = Column(Integer, ForeignKey('station.id'))
    origin = relationship("Station", foreign_keys=[origin_id])

    destination_id = Column(Integer, ForeignKey('station.id'))
    destination = relationship("Station", foreign_keys=[destination_id])
    created_at = Column(DateTime)

    def __init__(self, name:str, origin_id:int, destination_id:int):
        self.name = name
        self.origin_id = origin_id
        self.destination_id = destination_id
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Span(name='%s')>" % (self.name)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
