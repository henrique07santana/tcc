
from models.person import Person
from models.passenger import Passenger

from database import Database
from models.base import Base

db = Database()

engine = db.create_engine()
session = db.create_session()

Base.metadata.create_all(engine)


santana = Person("Henrique Santana", "henrique07santana@hotmail.com")
santana.add(session)

# session.add(santana)
# session.commit()
# print(santana.id, santana.name)

# metadata = MetaData()

# person = Table(PERSON, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('email', String)
#                     )
# users = Table(USERS, metadata,
#                     Column('person_id', Integer, primary_key=True),
#                     Column('password', String)
#                     )

# passengers = Table(PASSENGERS, metadata,
#                     Column('person_id', Integer, primary_key=True),
#                     Column('document', String)
#                     )

# vehicles = Table(VEHICLES, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('capacity', Integer)
#                     )        
# stations = Table(STATIONS, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String)
#                     )

# tickets = Table(TICKETS, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('passenger_id', Integer),
#                     Column('seat', Integer),
#                     Column('transit_id', Integer)
#                     )

# spans = Table(SPANS, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('origin_id', Integer),
#                     Column('destination_id', Integer)
#                     )

# gates = Table(GATES, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('number', Integer)
#                     )                

# transits = Table(TRANSITS, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('span_id', Integer)
#                     )

# routes = Table(ROUTES, metadata,
#                     Column('id', Integer, primary_key=True)
#                     )

# bookings = Table(BOOKINGS, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('origin_id', Integer),
#                     Column('destination_id', Integer)
#                     )
# try:
#     metadata.create_all(self.db_engine)
#     print("Tables created")
# except Exception as e:
#     print("Error occurred during Table creation!")
#     print(e)