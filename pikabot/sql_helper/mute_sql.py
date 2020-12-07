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

from . import SESSION, BASE
from sqlalchemy import *

class Mute(BASE):
    __tablename__ = "mute"
    sender = Column(String(14), primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    pika_id = Column(Numeric, primary_key = True)

    def __init__(self, sender, chat_id, pika_id):
        self.sender = str(sender)
        self.chat_id = str(chat_id)
        self.pika_id= pika_id

Mute.__table__.create(checkfirst=True)


def is_muted(sender, chat_id, pika_id):
    user = SESSION.query(Mute).get((str(sender), str(chat_id), pika_id))
    if user:
        return True
    else:
        return False


def mute(sender, chat_id, pika_id):
    adder = Mute(str(sender), str(chat_id), pika_id)
    SESSION.add(adder)
    SESSION.commit()


def unmute(sender, chat_id, pika_id):
    rem = SESSION.query(Mute).get((str(sender), str(chat_id), pika_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()

def get_all_muted(pika_id):
    rem = SESSION.query(Mute).filter(Notes.pika_id==pika_id).all()
    SESSION.close()
    return rem
