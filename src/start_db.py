import datetime as dt
from database import Database
from models.base import Base
from models.boarding_gate import BoardingGate
from models.booking import Booking
from models.passenger import Passenger
from models.person import Person
from models.route import Route
from models.seat import Seat
from models.span import Span
from models.station import Station
from models.ticket import Ticket
from models.transit import Transit
from models.user import User
from models.vehicle_type import VehicleType
from models.vehicle import Vehicle

db = Database()

engine = db.create_engine()
session = db.create_session()

Base.metadata.create_all(engine)

# Vehicle Type
vehicle_type_1_name = 'aeronave'
vehicle_type_1_brand = 'Boeing'
vehicle_type_1_model = '737-800'
vehicle_type_1_capacity = 186
vehicle_type_1_columns = 2
vehicle_type_1_seats_per_columns = 3
vehicle_type_1_category = 'nacional'

vehicle_type_1 = VehicleType(vehicle_type_1_name, 
                             vehicle_type_1_brand, 
                             vehicle_type_1_model, 
                             vehicle_type_1_capacity, 
                             vehicle_type_1_columns, 
                             vehicle_type_1_seats_per_columns, 
                             vehicle_type_1_category
                             )

vehicle_type_1.add(session) 
vehicle_type_1_id = vehicle_type_1.id

# Seats
seats_category = ['A', 'B', 'C', 'D', 'E', 'F']
vehicle_type_1_rows = int(vehicle_type_1_capacity / vehicle_type_1_columns * vehicle_type_1_seats_per_columns)
vehicle_type_1_seats_name_list = [str(i)+j for i in range(1,vehicle_type_1_rows+1) for j in seats_category]
vehicle_type_1_seats_number_list = list(range(1,vehicle_type_1_capacity+1))
result = [Seat(name, number, vehicle_type_1_id).add(session) for name, number in zip(vehicle_type_1_seats_name_list, vehicle_type_1_seats_number_list)]


# Station
station_1 = Station('Guarulhos')
station_1.add(session) 
station_1_id = station_1.id

station_2 = Station('Brasilia')
station_2.add(session) 
station_2_id = station_2.id

# Boarding Gate
result = [BoardingGate(gate, station_1_id).add(session) for gate in range(1, 26)]

# Span
span_1 = Span('Guarulhos-Brasilia', station_1_id, station_2_id)
span_1.add(session) 
span_1_id = span_1.id

# Person
person_1 = Person("Henrique Santana", "12345678910")
person_1.add(session)
person_1_id = person_1.id

# User
user_1 = User(person_1_id, 'henrique07santana@hotmail.com', '1234')
user_1.add(session)
user_1_id = user_1.id

# Passenger
passenger_1 = Passenger(person_1_id)
passenger_1.add(session)
passenger_1_id = passenger_1.id

# Booking
booking_1 = Booking(user_1_id)
booking_1.add(session)
booking_1_id = booking_1.id

# Route
route_1 = Route(station_1_id, station_2_id, booking_1_id)
route_1.add(session)
route_1_id = route_1.id

# Transit
transit_1 = Transit(dt.datetime.strptime('2020-10-12 10:30','%Y-%m-%d %H:%M'), route_1_id, span_1_id, vehicle_type_1_id)
transit_1.add(session)
transit_1_id = transit_1.id

# BoardingGate.get(session, 25)

# Ticket
ticket_1 = Ticket(transit_1_id, 78000, Seat.get(session, 4).id, passenger_1_id, booking_1_id)
ticket_1.add(session)
ticket_1_id = ticket_1.id
