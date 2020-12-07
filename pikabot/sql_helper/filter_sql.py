# © 2020 PikaBot
#
# You may not use this file without proper authorship and consent from @ItzSjDudeSupport
#
# Made by @ItzSjDude for Pikabot


from sqlalchemy import Column, UnicodeText, LargeBinary, Numeric, String
from pikabot.sql_helper import SESSION, BASE

class Filters(BASE):
    __tablename__ = "filters"
    chat_id = Column(String(14), primary_key=True)
    keyword = Column(UnicodeText, primary_key=True)
    pika_id = Column(Numeric, primary_key=True)
    reply = Column(UnicodeText)
    snip_type = Column(Numeric)
    media_id = Column(UnicodeText)
    media_access_hash = Column(UnicodeText)
    media_file_reference = Column(LargeBinary)

    def __init__(
        self,
        chat_id,
        keyword, reply, snip_type,
        media_id=None, media_access_hash=None, media_file_reference=None, pika_id
    ):
        self.chat_id = chat_id
        self.keyword = keyword
        self.reply = reply
        self.pika_id = pika_id 
        self.snip_type = snip_type
        self.media_id = media_id
        self.media_access_hash = media_access_hash
        self.media_file_reference = media_file_reference
   

Filters.__table__.create(checkfirst=True)

def get_filter(chat_id, keyword, pika_id):
    try:
        return SESSION.query(Filters).get((str(chat_id), keyword, pika_id))
    except:
        return None
    finally:
        SESSION.close()


def get_all_filters(chat_id, pika_id):
    try:
        return SESSION.query(Filters).filter(Filters.chat_id == str(chat_id), Filters.pika_id == pika_id).all()
    except:
        return None
    finally:
        SESSION.close()


def add_filter(chat_id, keyword, reply, snip_type, media_id, media_access_hash, media_file_reference, pika_id):
    adder = SESSION.query(Filters).get((str(chat_id), keyword, pika_id))
    if adder:
        adder.reply = reply
        adder.pika_id = pika_id
        adder.snip_type = snip_type
        adder.media_id = media_id
        adder.media_access_hash = media_access_hash
        adder.media_file_reference = media_file_reference
    else:
        adder = Filters(chat_id, keyword, reply, snip_type, media_id,
                        media_access_hash, media_file_reference, pika_id)
    SESSION.add(adder)
    SESSION.commit()


def remove_filter(chat_id, keyword, pika_id):
    saved_filter = SESSION.query(Filters).get((str(chat_id), keyword, pika_id))
    if saved_filter:
        SESSION.delete(saved_filter)
        SESSION.commit()


def remove_all_filters(chat_id, pika_id):
    saved_filter = SESSION.query(Filters).filter(Filters.chat_id == str(chat_id), Filters.pika_id=pika_id)
    if saved_filter:
        saved_filter.delete()
        SESSION.commit()

