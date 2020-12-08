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

from .sql_helper import pmpermit_sql, notes_sql, gmute_sql, locks_sql, filter_sql, snips_sql, welcome_sgl; pikapm=pmpermit_sql.PMPermit.__table__; pikanotes = notes_sql.Notes.__table__; pikagmt = gmute_sql.GMute.__table__; pikalock = locks_sql.Locks.__table__; pikafilter=filter_sql.Filters.__table__; pikasnip=snips_sql.Snips.__table__; pikawelcm=welcome_sql.Welcome.__table__

def pika_db_reset():
    pikapm.drop()
    pikanotes.drop()
    pikagmt.drop()
    pikalocks.drop()
    pikafilter.drop()
    pikasnip.drop()
    pikawelcm.drop()
