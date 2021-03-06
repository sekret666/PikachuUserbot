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

from . import BASE, SESSION


class PikaChats(BASE):
    __tablename__ = "PikaTg"
    pika_id = Column(String(14), primary_key=True)

    def __init__(self, pika_id):
        self.pika_id = pika_id


PikaChats.__table__.create(checkfirst=True)

def add_pika(pika_id):
    pika = PikaChats(str(pika_id))
    SESSION.add(pika)
    SESSION.commit()

def is_pika_exist(pika_id):
    try:
       pika = SESSION.query(PikaChats).filter(PikaChats.pika_id == str(pika_id)).one()
       if pika:  
           return True   
    except:
       return None
    finally:
       SESSION.close()

def get_pika_chats():
    try: 
       pika = SESSION.query(PikaChats).all()
       if pika:
           return pika
    except:
       return None
    finally: 
       SESSION.close()
