from typing import Dict
from sqlalchemy import and_

class Model:    
    """id tem que ser implementado quando herdado"""
    @classmethod
    def get(cls, session, id:int):
        result = session.query(cls).filter(cls.id == id).first()
        return result

    @classmethod
    def update(cls, session, id:int, field:str, value:str):
        session.query(cls).filter(cls.id == id).update({field: value})
        session.commit()
        print(cls.__name__, ' ', 'id: ', id,  ' updated ',  field, ' to ', value)

    @classmethod
    def delete(cls, session, id:int):
        session.query(cls).filter(cls.id==id).delete()
        session.commit()

    @classmethod
    def filter(cls, session, **kwargs):
        filters = kwargs
        query = session.query(cls)
        for attr,value in filters.items():
            query = query.filter( getattr(cls,attr)==value)
        result = query.first()
        return result