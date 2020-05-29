from sqlalchemy import Column, Integer, String, DateTime, Sequence, ForeignKey
from sqlalchemy.orm import relationship
from typing import Dict
from datetime import datetime
import os
import sys
sys.path.append(os.path.realpath('.'))
from models.base import Base
from models.model import Model
from models.span import Span
from models.route import Route

table_name = 'station'

class Station(Base, Model):
    __tablename__ = table_name
    id = Column(Integer, Sequence('station_id_seq'), primary_key=True)
    name = Column(String(50))
    created_at = Column(DateTime)

    def __init__(self, name:str):
        self.name = name
        self.created_at = datetime.now()

    def __repr__(self):
        return "<Station(name='%s')>" % (self.name)

    def add(self, session):
        session.add(self)
        session.commit()
        print(table_name, ' ', self.id, ' created')
        return self.id
