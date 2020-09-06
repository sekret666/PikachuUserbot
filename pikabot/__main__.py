import os, telethon, telethon.utils, asyncio, traceback ; from pikabot import * ; from sys import * ; from var import * ; client = bot ; ItzSjDude = client ; from telethon.errors.rpcerrorlist import * ; from var import Client as clIent ; from pathlib import Path ; from telethon import * ; from telethon.tl.types import * 
async def add_bot(bot_token):
    await bot.start(bot_token)
    await bot2.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)
    bot.axi = await bot2.get_me()
    bot.bxi = telethon.utils.get_peer_id(bot.axi)
    ax = bot.me.first_name

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient("TG_BOT_TOKEN",api_id=Var.APP_ID,api_hash=Var.API_HASH).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()

async def alt():
    await bot.start()
    LOGS.info("Detecting nd Connecting to Sessions...")
    if bot2:
        try:
            await bot2.start()
            LOGS.info("String 2 Connected")
        except:
            LOGS.info("String Session 2 expired. Please create new one")
            quit(1)
    if bot3:
        try:
            await bot3.start()
            LOGS.info("Session 3 Connected")
        except:
            LOGS.info("String Session 2 expired. Please create new one")
            quit(1)
    if bot4:
        try:
            await bot4.start()
            LOGS.info("Session 4 Connected")
        except:
            LOGS.info("String Session 4 expired. Please create new one")
            quit(1)
  
    cli1 = await client.get_messages(clIent, None , filter=InputMessagesFilterDocument) ; total = int(cli1.total) ; total_doxx = range(0, total)
    for ixo in total_doxx:
       mxo =cli1[ixo].id ; await client.download_media(await bot.get_messages(clIent, ids=mxo), "pikabot/main_plugs")
bot.loop.run_until_complete(alt())

import pikabot._core
LOGS.info("Initialising Core")

import pikabot.carbonX   
LOGS.info("setting up carbon") 

from pikabot.utils import load_module
path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


LOGS.info(f"{ax}'s Pikabot activated successfully type {l}help or {l}alive in Saved Messages")
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
