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
#
# Made by @ItzSjDude for Pikabot

from sqlalchemy import *
from . import SESSION, BASE

class Welcome(BASE):
    __tablename__ = "welcome"
    chat_id = Column(String(14), primary_key=True)
    pika_id = Column(Numeric, primary_key=True)
    cust_wc = Column(UnicodeText)
    cl_wc = Column(Boolean, default=False)
    prev_wc = Column(BigInteger)
    mf_id = Column(UnicodeText)

    def __init__(self, chat_id, pika_id, cust_wc, cl_wc, prev_wc, mf_id=None):
        self.chat_id = chat_id
        self.pika_id = pika_id
        self.cust_wc = cust_wc
        self.cl_wc = cl_wc
        self.prev_wc = prev_wc 
        self.mf_id = mf_id
        
Welcome.__table__.create(checkfirst=True)

def add_welcome(chat_id, pika_id, cust_wc, cl_wc, prev_wc, mf_id):
    add_wc = Welcome(chat_id, pika_id, cust_wc, cl_wc, prev_wc, mf_id)
    SESSION.add(add_wc)
    SESSION.commit()

def remove_welcome(chat_id):
    rm_wc = SESSION.query(Welcome).get((str(chat_id), pika_id))
    if rm_wc:
        SESSION.delete(rem)
        SESSION.commit()

def upd_prev_welcome(chat_id, pika_id, prev_wc):
    get = SESSION.query(Welcome).get(chat_id, pika_id)
    get.prev_wc = prev_wc
    SESSION.commit()

def get_welcome(chat_id, pika_id):
    try:
        return SESSION.query(Welcome).filter((Welcome.chat_id == str(chat_id), Welcome.pika_id == pika_id)).one()
    except:
        return None
    finally:
        SESSION.close()
