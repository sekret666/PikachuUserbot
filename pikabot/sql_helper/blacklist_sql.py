import threading

from sqlalchemy import func, distinct, Column, String, UnicodeText

from userbot.plugins.sql_helper import SESSION, BASE


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


BLF2.__table__.create(checkfirst=True)

class BLF2(BASE):
    __tablename__ = "blst"
    chat_id = Column(String(14), primary_key=True)
    trigger = Column(UnicodeText, primary_key=True, nullable=False)

    def __init__(self, chat_id, trigger):
        self.chat_id = str(chat_id)  # ensure string
        self.trigger = trigger

    def __repr__(self):
        return "<Blacklist filter '%s' for %s>" % (self.trigger, self.chat_id)

    def __eq__(self, other):
        return bool(isinstance(other, BLF2)
                    and self.chat_id == other.chat_id
                    and self.trigger == other.trigger)


BLF2.__table__.create(checkfirst=True)


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

def a_to_bl(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = BLF2(str(chat_id), trigger)

        SESSION.merge(blacklist_filt)  # merge to avoid duplicate key issues
        SESSION.commit()
        CHAT_BLACKLISTS.setdefault(str(chat_id), set()).add(trigger)


def rf_bl(chat_id, trigger):
    with BLACKLIST_FILTER_INSERTION_LOCK:
        blacklist_filt = SESSION.query(BLF2).get((str(chat_id), trigger))
        if blacklist_filt:
            if trigger in CHAT_BLACKLISTS.get(str(chat_id), set()):  # sanity check
                CHAT_BLACKLISTS.get(str(chat_id), set()).remove(trigger)

            SESSION.delete(blacklist_filt)
            SESSION.commit()
            return True

        SESSION.close()
        return False


def gc_bl(chat_id):
    return CHAT_BLACKLISTS.get(str(chat_id), set())


def no_blf():
    try:
        return SESSION.query(BLF2).count()
    finally:
        SESSION.close()


def n_bl_cf(chat_id):
    try:
        return SESSION.query(BLF2.chat_id).filter(BLF2.chat_id == str(chat_id)).count()
    finally:
        SESSION.close()


def n_bl_fc():
    try:
        return SESSION.query(func.count(distinct(BLF2.chat_id))).scalar()
    finally:
        SESSION.close()


def __lc_bl():
    global CHAT_BLACKLISTS
    try:
        chats = SESSION.query(BLF2.chat_id).distinct().all()
        for (chat_id,) in chats:  # remove tuple by ( ,)
            CHAT_BLACKLISTS[chat_id] = []

        all_filters = SESSION.query(BLF2).all()
        for x in all_filters:
            CHAT_BLACKLISTS[x.chat_id] += [x.trigger]

        CHAT_BLACKLISTS = {x: set(y) for x, y in CHAT_BLACKLISTS.items()}

    finally:
        SESSION.close()


__lc_bl()


