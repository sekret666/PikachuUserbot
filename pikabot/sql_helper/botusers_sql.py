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


class BotUsers(BASE):
    __tablename__ = "botusers"
    pika_id = Column(String(14), primary_key=True)

    def __init__(self, pika_id):
        self.pika_id = pika_id


BotUsers.__table__.create(checkfirst=True)


def add_user(pika_id: int):
    pika = BotUsers(str(pika_id))
    SESSION.add(pika)
    SESSION.commit()


def is_user_exist(pika_id):
    pika = SESSION.query(BotUsers).filter(BotUsers.pika_id == str(pika_id)).one()
    if pika:
        try: 
          return True   
        except:
          return None
        finally:
          SESSION.close()

def get_added_users():
    pika = SESSION.query(BotUsers).all()
    SESSION.close()
    return pika
