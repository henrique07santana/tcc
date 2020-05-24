from typing import Dict

class Model:

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
