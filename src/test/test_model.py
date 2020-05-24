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
from models.person import Person
from models.passenger import Passenger

test_db = Database(db_type='test')
engine = test_db.create_engine()
Base.metadata.create_all(engine)
session = test_db.create_session()


class TestModel(unittest.TestCase):

    def test_create_person(self):
        santana = Person("Henrique Santana", "henrique07santana@hotmail.com")
        id = santana.add(session)
        self.assertIsInstance(id, int)
    
    def test_update_person(self):
        new_email = "henrique07santana@gmail.com"
        id = 1
        Person.update(session, id, 'email', new_email)
        result = Person.get(session, id)
        print(result)
        self.assertEqual(result.email, new_email)

    def test_create_passenger(self):
        santana = Passenger(1, "12345678910")
        id = santana.add(session)
        self.assertIsInstance(id, int)

if __name__ == "__main__":
    unittest.main()
