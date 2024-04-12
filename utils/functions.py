import urllib
import json
import time
from datetime import datetime


def json_decoder(text):
    return json.loads(text)


def html_decoder(text):
    text = urllib.parse.unquote(text)
    text = text.replace("+", " ") if (text.count("+") > 1) and (text.isspace() is not True) else text
    return text


def get_time(timestamp, date_format="%d/%m/%Y - %H:%M"):
    return datetime.fromtimestamp(timestamp/1000.0).strftime(date_format)


def get_current_timestamp():
    return round(time.time()*1000)