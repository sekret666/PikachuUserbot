#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 


from sqlalchemy import * 
from . import SESSION, BASE

class PMPermit(BASE):
    __tablename__ = "pmpermit"
    chat_id = Column(String(14), primary_key=True)
    reason = Column(String(127))
    pika_id = Column(Numeric, primary_key=True)
    def __init__(self, chat_id, pika_id, reason=""):
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

