from . import context, message, sender

BOT_NAME = "botname"
CHANNEL = "channel"
CONTEXT = "contextobj"
SENDER = "senderobj"
MESSAGE = "messageobj"


class INPUT(object):
    def __init__(self, info):
        self.info = info
        self.bot_name = info[BOT_NAME] if self.exists(BOT_NAME) else None
        self.channel = info[CHANNEL] if self.exists(CHANNEL) else None
        self.context = context.Context(info[CONTEXT]) if self.exists(CONTEXT) else None
        self.sender = sender.Sender(info[SENDER]) if self.exists(SENDER) else None
        if self.exists(MESSAGE):
            if info[MESSAGE]["type"] == "text":
                self.message = message.MessageText(info[MESSAGE])
            elif info[MESSAGE]["type"] == "image":
                self.message = message.MessageImage(info[MESSAGE])
        else:
            self.message = None

    def exists(self, key):
        return key in self.info

    def __str__(self):
        return str(self.info)

    def __repr__(self):
        return str(self.info)
