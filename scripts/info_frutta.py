
info = dict(
        name="Info Frutta",
        author="pankapuzza",
        version="1.0",
        description="Script risponditore automatico per informazioni sulla frutta",
        events={},
        #events={"MessageReceived": on_message_received},
        main=None,
    )


class InfoBot(object):
    def __init__(self, bot):
        self.bot = bot
        self.prefix = "info_frutta: "

    def run(self):
        print(self.prefix+" loaded!")
        info["events"] = {"MessageReceived": self.on_message}
        print(info["events"])

    def on_message(self, bot, inboud):
        return self.prefix+inboud.message.text


def get_script_info():
    if info["main"] is None:
        info["main"] = InfoBot

    return info