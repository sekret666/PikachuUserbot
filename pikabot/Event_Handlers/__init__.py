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

import asyncio,os,sys,heroku3; from telethon import TelegramClient, events, custom; from telethon.sessions import StringSession; from telethon.errors.rpcerrorlist import *; from var import Var

Heroku = heroku3.from_key(Var.HEROKU_API_KEY);app = Heroku.app(Var.HEROKU_APP_NAME)
from .logit import pikalog

def get_client(_Pika_):
    global a
    if _Pika_=="STRING_SESSION":
       a ="**MAINCLIENT**"
    elif _Pika_=="STR2":
      a ="**MULTICLIENT1**"
    elif _Pika_=="STR3":
      a ="**MULTICLIENT2**"
    elif _Pika_=="STR4":
      a ="**MULTICLIENT3**"
    return a
