from pprint import pprint


class Main(object):
    def __init__(self, bot):
        self.bot = bot

    def run(self):
        url = "https://filemanager.gupshup.io/fm/wamedia/demobot1/e1f59f90-266b-4b06-bbd7-c632cea3074e"
        self.bot.send_msg("xxxxx", url)
        #self.bot.send_img("xxxx", url, url, "test")


def on_message_received(bot, inboud):

    pprint(inboud)

    sender = inboud.context.sender_name
    message_type = inboud.message.type

    if message_type == "text":
        message_text = inboud.message.text
        return "Ciao "+sender+", Hai scritto: "+message_text
    elif message_type == "image":
        number = inboud.context.cc+inboud.context.dc
        image = inboud.message.image.url
        bot.send_img(number, image, image, inboud.message.caption)
        return "Ciao "+sender+", Bella foto!"
    return None


def get_script_info():
    return dict(
        name="test",
        author="pankapuzza",
        version="1.0",
        description="Script for test inboud messages",
        events={},
        #events={"MessageReceived": on_message_received},
        main=Main,
    )
