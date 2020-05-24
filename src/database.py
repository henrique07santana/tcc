from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import variables

class Database:
    def __init__(self, db_type='live'):
        self.db_url = variables['LIVE_DB_URL']
        if db_type != 'live':
            self.db_url = variables['TEST_DB_URL']
    
    def create_engine(self):
        engine = create_engine(self.db_url , echo=True)
        return engine
    
    def create_session(self):
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    

#     def create_db_tables(self, column_list):

#         person = Table(PERSON, metadata,
#                     Column('id', Integer, primary_key=True),
#                     Column('name', String),
#                     Column('email', String)
#                     )


 
#  if __name__ == '__main__':
#     dbms = Database(SQLITE, dbname=DBNAME)
#     dbms.create_db_tables()