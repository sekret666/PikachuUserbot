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

import os 
from functools import wraps
TGBOT_USERS = set(int(x) for x in os.environ.get("BOT_USERS", "779890498").split())
from pikabot.main_plugs.utils import *
from pikabot.sql_helper.chats_sql import *
from importlib.util import *
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
def pikatgbot(pika=None, silent=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(event):
            _selfpika = await tgbot.get_me()
            if "AdmOnly" in pika:
                _pika = await tgbot.get_permissions(event.chat_id, event.sender_id)
                if _pika.is_admin:
                    await func(event)
                if event.sender_id == bot.uid:
                    pass
                if not _pika.is_admin:
                    if silent is None:
                        await event.reply("You need to be admin to use this command")

            if "AmIAdm" in pika:

                _pika = await tgbot.get_permissions(event.chat_id, _selfpika.id)
                if _pika.is_admin:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("I am not Admin Nibba😷")

            if "OwnSudo" in pika:
                tgbotusers = list(TGBOT_USERS)
                if event.sender_id == bot.uid or event.sender_id == tgbotusers:
                    await func(event)
                else:
                    if silent is None:
                        await event.reply("**Error**: You are not a Sudo User, Owner.")

            if "Owner" in pika:
                if event.sender_id == bot.uid:
                    await func(event)
                else:
                    if silent is None: 
                        await event.reply("Only Owners can execute this Cmd")

            if "BotSudo" in pika:
                if event.sender_id == list(TGBOT_USERS):
                    await func(event)

        return wrapper

    return decorator

#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def pika_msg(self, text, _pika_=None):
  if _pika_ is None:
      return await self.edit(text)
  else:
      return await self.reply(text)
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/> 
async def is_pikatg(_pika_=None):
  _pika = await _pika_.client.get_me()
  if _pika.id== tgbot.uid:
      return True
  else:
      return False
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_id(_pika):
  _pika_= await _pika.client.get_me() 
  return _pika_.id 
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
async def get_pika_tg(_pika_): 
  _tg = await _pika_.client.get_me()
  if _tg.id == tgbot.uid:
      return True
  else:
      return None
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
def add_chat(_pika_):
  if _pika_.client == tgbot:
    if not _pika_.is_private:
      if not is_pika_exist(_pika_): 
        add_pika(_pika_.chat_id)
        return "Added" 
  else:
    return
 
#©ItzSjDude </Kang/Copy with Credits else u will be called ultra gey/>
def pika_assistant(_pikasst):
    if ACTIVATE_ASSISTANT:
                                    #____Imports____
       import sys           
       import pikabot.utils
       from sys import modules
       from __main__ import l as rx
       from pathlib import Path as _asstpath
       import plugins.__init__ as Modules
       logpa.info('✨STARTING PIKA ASSISTANT✨')
                                    #____Paths/Spec_____
       asstpath = _asstpath(f"pikabot/Assistant/plugins/{_pikasst}.py")
       asstname = "pikabot.Assistant.plugins.{}".format(_pikasst)
       spec = spec_from_file_location(asstname, asstpath)
       asst = module_from_spec(spec)
                                   #____Pika_Assistant_Plugins_Loader____
       if _pikasst.startwith('__'):
           userbot = pikabot; asst.bot = bot; asst.tgbot = tgbot; asst.Var = Var; asst.rx = rx; asst.ItzSjDude = ItzSjDude;
           spec.loader.exec_module(asst)
           PikaAsst[_pikasst] = asst; modules['Asst_modules'] = Modules ; modules["pikabot"+_pikasst] = asst; logpa.info("🔥Imported "+_pikasst)
       else:
          pass 
    else: 
       return 
