#  © Pikabot
#
# You may not use this file without proper authorship and consultant from @ItzSjDudeSupport
#
# Made By @ItzSjDude for Pikabot

import threading
from sqlalchemy import func, distinct, Column, String, UnicodeText
from pikabot.sql_helper import SESSION, BASE

class BlackListFilters(BASE):
    __tablename__ = "blacklist"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, BlackListFilters)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


BlackListFilters.__table__.create(checkfirst=True)

class Blfx(BASE):
    __tablename__ = "blacklistx"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, Blfx)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


Blfx.__table__.create(checkfirst=True)

class Blfy(BASE):
    __tablename__ = "blacklisty"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, Blfy)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


Blfy.__table__.create(checkfirst=True)

class Blfz(BASE):
    __tablename__ = "blacklistz"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, Blfz)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


Blfz.__table__.create(checkfirst=True)



BLACKLIST_FILTER_INSERTION_LOCK = threading.RLock()

CHAT_BLACKLISTS = {}


def add_to_blacklist(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = BlackListFilters(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLISTS.setdefault(str(chat_id), set()).add(trigger)


def rm_from_blacklist(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(BlackListFilters).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def get_chat_blacklist(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())


def num_blacklist_filters():
    try:
        return SESSION.query(BlackListFilters).count()
    finally:
        SESSION.close()


def num_blacklist_chat_filters(chat_id):
    try:
        return SESSION.query(BlackListFilters.chat_id).filter(BlackListFilters.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def num_blacklist_filter_chats():
    try:
        return SESSION.query(func.count(distinct(BlackListFilters.chat_id))).scalar()
    finally:
        SESSION.close()


def __load_chat_blacklists():
    global CHAT_BLACKLISTS
    try:
        chats = SESSION.query(BlackListFilters.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLISTS[chat_id] = []

        all_filters = SESSION.query(BlackListFilters).all()
        for x in all_filters:
            CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

        CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}

    finally:
        SESSION.close()


__load_chat_blacklists()

def a_to_blx(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = Blfx(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLISTS.setdefault(str(chat_id), set()).add(trigger)


def rf_blx(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(Blfx).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def gc_blx(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())


def no_blfx():
    try:
        return SESSION.query(Blfx).count()
    finally:
        SESSION.close()


def n_bl_cfx(chat_id):
    try:
        return SESSION.query(Blfx.chat_id).filter(Blfx.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def n_bl_fcx():
    try:
        return SESSION.query(func.count(distinct(Blfx.chat_id))).scalar()
    finally:
        SESSION.close()


def __lc_blx():
    global CHAT_BLACKLISTS
    try:
        chats = SESSION.query(Blfx.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLISTS[chat_id] = []

        all_filters = SESSION.query(Blfx).all()
        for x in all_filters:
            CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

        CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}

    finally:
        SESSION.close()


__lc_blx()

def a_to_bly(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = Blfy(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLISTS.setdefault(str(chat_id), set()).add(trigger)


def rf_bly(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(Blfy).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def gc_bly(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())


def no_blfy():
    try:
        return SESSION.query(Blfy).count()
    finally:
        SESSION.close()


def n_bl_cfy(chat_id):
    try:
        return SESSION.query(Blfy.chat_id).filter(Blfy.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def n_bl_fcy():
    try:
        return SESSION.query(func.count(distinct(Blfy.chat_id))).scalar()
    finally:
        SESSION.close()


def __lc_bly():
    global CHAT_BLACKLISTS
    try:
        chats = SESSION.query(Blfy.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLISTS[chat_id] = []

        all_filters = SESSION.query(Blfy).all()
        for x in all_filters:
            CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

        CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}

    finally:
        SESSION.close()


__lc_bly()

def a_to_blz(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = Blfz(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLISTS.setdefault(str(chat_id), set()).add(trigger)


def rf_blz(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(Blfz).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def gc_blz(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())


def no_blfz():
    try:
        return SESSION.query(Blfz).count()
    finally:
        SESSION.close()


def n_bl_cfz(chat_id):
    try:
        return SESSION.query(Blfz.chat_id).filter(Blfz.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def n_bl_fcz():
    try:
        return SESSION.query(func.count(distinct(Blfz.chat_id))).scalar()
    finally:
        SESSION.close()


def __lc_blz():
    global CHAT_BLACKLISTS
    try:
        chats = SESSION.query(Blfz.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLISTS[chat_id] = []

        all_filters = SESSION.query(Blfz).all()
        for x in all_filters:
            CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

        CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}

    finally:
        SESSION.close()


__lc_blz()



