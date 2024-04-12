C_ID = "channelid"
C_TYPE = "channeltype"
DISPLAY = "display"
SUB_DISPLAY = "subdisplay"


class Sender(object):
    def __init__(self, raw):
        self.raw = raw
        self.channel_id = raw[C_ID] if self.exists(C_ID) else None
        self.channel_type = raw[C_TYPE] if self.exists(C_ID) else None
        self.display = raw[DISPLAY].replace("+", " ") if self.exists(DISPLAY) else None
        self.sub_display = raw[SUB_DISPLAY].replace("+", " ") if self.exists(SUB_DISPLAY) else None

    def exists(self, key):
        return key in self.raw

    def __str__(self):
        return str(self.raw)

    def __repr__(self):
        return str(self.raw)
