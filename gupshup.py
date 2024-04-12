import settings
from connections.bot import API
from connections.callback_server import *
from utils import chat, exceptions
import os
import sys

bot = API(settings.API_INFO["BOT_NAME"],
          settings.API_INFO["KEY"],
          settings.API_INFO["NUMBER"])


scripts = []

if settings.CUSTOM_SCRIPTS["ENABLE"]:
    sys.path.insert(0, settings.CUSTOM_SCRIPTS["PATH"])
    for file in os.listdir(settings.CUSTOM_SCRIPTS["PATH"]):
        if file.endswith(".py"):
            file_name = file[:-3]
            if file_name not in settings.CUSTOM_SCRIPTS["SCRIPTS"]:
                continue
            script = __import__(file_name)
            try:
                info = script.get_script_info()
                chat.log("Loading script: "+info["name"]+", v: "+info["version"])
                if info["main"] is not None:
                    info["main"](bot).run()
                scripts.append(script)
            except exceptions.NotAScript:
                chat.error("The file: "+file+" is not a script")


if settings.SERVER["ENABLE"]:
    run_server(chat, bot, scripts)


"""msg = bot.send_msg("393288071822", "ciao papino")

print("status: " + msg["status"])
print("id: " + msg["messageId"])"""
