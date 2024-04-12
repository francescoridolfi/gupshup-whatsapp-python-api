from .context import Context

MSG_TEXT_FROM = "from"
MSG_TEXT_ID = "id"
MSG_TEXT_TEXT = "text"
MSG_TEXT_T_S = "timestamp"
MSG_TEXT_TYPE = "type"

IMG_BOT_NAME = "botname"
IMG_CONTEXT = "contextObj"
IMG_MEDIA = "mediaId"
IMG_URL = "url"

MSG_IMG_CAPTION = "caption"
MSG_IMG_FROM = "from"
MSG_IMG_ID = "id"
MSG_IMG_IMG = "imgData"
MSG_IMG_TEXT = "text"
MSG_IMG_T_S = "timestamp"
MSG_IMG_TYPE = "type"
MSG_IMG_URL = "url"


class MessageText(object):
    def __init__(self, raw):
        self.raw = raw
        self.sender = raw[MSG_TEXT_FROM] if self.exists(MSG_TEXT_FROM) else None
        self.id = raw[MSG_TEXT_ID] if self.exists(MSG_TEXT_ID) else None
        self.text = raw[MSG_TEXT_TEXT] if self.exists(MSG_TEXT_TEXT) else None
        self.timestamp = raw[MSG_TEXT_T_S] if self.exists(MSG_TEXT_T_S) else None
        self.type = raw[MSG_TEXT_TYPE] if self.exists(MSG_TEXT_TYPE) else None

    def exists(self, key):
        return key in self.raw

    def __str__(self):
        return str(self.raw)

    def __repr__(self):
        return str(self.raw)


class Image(object):
    def __init__(self, raw):
        self.raw = raw
        self.bot_name = raw[IMG_BOT_NAME] if self.exists(IMG_BOT_NAME) else None
        self.context = Context(raw[IMG_CONTEXT]) if self.exists(IMG_CONTEXT) else None
        self.media_id = raw[IMG_MEDIA] if self.exists(IMG_MEDIA) else None
        self.url = raw[IMG_URL] if self.exists(IMG_URL) else None

    def exists(self, key):
        return key in self.raw

    def __str__(self):
        return str(self.raw)

    def __repr__(self):
        return str(self.raw)


class MessageImage(object):
    def __init__(self, raw):
        self.raw = raw
        self.caption = raw[MSG_IMG_CAPTION] if self.exists(MSG_IMG_CAPTION) else None
        self.sender = raw[MSG_IMG_FROM] if self.exists(MSG_IMG_FROM) else None
        self.id = raw[MSG_IMG_ID] if self.exists(MSG_IMG_ID) else None
        self.text = raw[MSG_IMG_TEXT] if self.exists(MSG_IMG_TEXT) else None
        self.image = Image(raw[MSG_IMG_IMG]) if self.exists(MSG_IMG_IMG) else None
        self.timestamp = raw[MSG_IMG_T_S] if self.exists(MSG_IMG_T_S) else None
        self.type = raw[MSG_IMG_TYPE] if self.exists(MSG_IMG_TYPE) else None
        self.url = raw[MSG_IMG_URL] if self.exists(MSG_IMG_URL) else None

    def exists(self, key):
        return key in self.raw

    def __str__(self):
        return str(self.raw)

    def __repr__(self):
        return str(self.raw)
