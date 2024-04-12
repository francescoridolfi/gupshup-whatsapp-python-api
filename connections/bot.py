import requests
from pprint import pprint

URL = "https://api.gupshup.io/sm/api/v1/"

SEND_MSG_URL = "msg"
GET_USERS_URL = "users/{bot_name}"

WHATSAPP_CHANNEL = "whatsapp"


class API(object):

    def __init__(self, bot_name, api_key, source, channel=None):
        self.bot_name = bot_name
        self.api_key = api_key
        self.source = source

        self.channel = channel or WHATSAPP_CHANNEL

        self.default_header = {
            "Cache-Control": "no-cache",
            "Content-type": "application/x-www-form-urlencoded",
            "apikey": api_key,
            "cache-control": "no-cache",
        }

    def send_msg(self, destination, text):
        payload = {
            "channel": self.channel,
            "source": self.source,
            "destination": destination,
            "message": text,
            "src.name": self.bot_name,
        }

        r = requests.post(URL+SEND_MSG_URL, headers=self.default_header, data=payload)
        return r.json()

    def send_img(self, destination, preview_url, original_url, caption=None):
        payload = {
            "channel": self.channel,
            "source": self.source,
            "destination": destination,
            "message.payload": {
                "originalUrl": original_url,
                "previewUrl": preview_url,
                "caption": caption,
            },
            "src.name": self.bot_name,
        }

        pprint(payload)

        r = requests.post(URL + SEND_MSG_URL, headers=self.default_header, data=payload)
        print(r.text)
        return r.text

    def get_users(self):
        req = URL+GET_USERS_URL.replace("{bot_name}", self.bot_name)

        r = requests.get(req, headers=self.default_header)
        return r.json()
