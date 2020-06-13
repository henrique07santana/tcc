import unittest
import os
import sys
import unittest

try:
    import context
except ModuleNotFoundError:
    import test.context    

from database import Database
from models.base import Base
from models.booking import Booking
from models.passenger import Passenger
from models.person import Person
from models.route import Route
from models.seat import Seat
from models.span import Span
from models.boarding_gate import BoardingGate
from models.station import Station
from models.ticket import Ticket
from models.transit import Transit
from models.user import User
from models.vehicle_type import VehicleType
from models.vehicle import Vehicle


test_db = Database(db_type='test')
engine = test_db.create_engine()
Base.metadata.create_all(engine)
session = test_db.create_session()


class TestModel(unittest.TestCase):

    def test_create_person(self):
        marcos = Person(name="Marcos Paulo", document="12345678910")
        person_id = marcos.add(session)
        self.assertIsInstance(person_id, int)
    
    def test_create_passenger(self):
        henrique = Person(name="Henrique Santana", document="10987654321")
        result = henrique.filter(session, name=henrique.name, document=henrique.document)
        if result != None:
            person_id = result.id
        else:
            person_id = henrique.add(session)
        passenger_henrique = Passenger(person_id=person_id, phone_number="21988889999")
        passenger_id = passenger_henrique.add(session)
        self.assertIsInstance(passenger_id, int)


    def test_update_person(self):
        henrique = Person(name="Henrique Santana", document="10987654321")
        new_doc = "99999999999"
        result = henrique.filter(session=session, name=henrique.name, document=henrique.document)
        person_id = result.id
        henrique.update(session=session, id=person_id, field='document', value=new_doc)
        result = Person.get(session=session, id=person_id)
        print(result)
        self.assertEqual(result.document, new_doc)

    def test_delete_person(self):
        marcos = Person(name="Marcos Paulo", document="12345678910")
        result = marcos.filter(session=session, name=marcos.name, document=marcos.document)
        person_id = result.id
        marcos.delete(session, person_id)
        result = Person.get(session=session, id=person_id)
        print(result)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
