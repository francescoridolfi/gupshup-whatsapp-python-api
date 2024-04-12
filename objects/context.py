BOT_NAME = "botname"
CC = "cc"
DC = "dc"
C_TYPE = "channeltype"
CONTEXT_ID = "contextid"
CONTEXT_TYPE = "contexttype"
SENDER = "senderName"


class Context(object):
    def __init__(self, raw):
        self.raw = raw
        self.bot_name = raw[BOT_NAME] if self.exists(BOT_NAME) else None
        self.cc = raw[CC] if self.exists(CC) else None
        self.dc = raw[DC] if self.exists(DC) else None
        self.channel_type = raw[C_TYPE] if self.exists(C_TYPE) else None
        self.context_id = raw[CONTEXT_ID] if self.exists(CONTEXT_ID) else None
        self.context_type = raw[CONTEXT_TYPE] if self.exists(CONTEXT_TYPE) else None
        self.sender_name = raw[SENDER].replace("+", " ") if self.exists(SENDER) else None

    def exists(self, key):
        return key in self.raw

    def __str__(self):
        return str(self.raw)

    def __repr__(self):
        return str(self.raw)
