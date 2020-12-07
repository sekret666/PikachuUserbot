from sqlalchemy import Column, String
from pikabot.sql_helper import SESSION, BASE

class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))
    pika_id = Column(Numeric, primary_key=True)
    def __init__(self, chat_id, reason="", pika_id):
        self.chat_id = chat_id
        self.reason = reason
        self.pika_id = pika_id

PMPermit.__table__.create(checkfirst=True)

def approve(chat_id, reason, pika_id):
    adder = PMPermit(str(chat_id), str(reason), pika_id)
    SESSION.add(adder)
    SESSION.commit()


def disapprove(chat_id, pika_id):
    rem = SESSION.query(PMPermit).get(str(chat_id), pika_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_all_approved(pika_id):
    rem = SESSION.query(PMPermit).filter(PMPermit.pika_id == pika_id).all()
    SESSION.close()
    return rem

def is_approved(chat_id, pika_id):
    try:
        return SESSION.query(PMPermit).filter(PMPermit.chat_id == str(chat_id), PMPermit.pika_id=pika_id).one()
    except:
        return None
    finally:
        SESSION.close()

