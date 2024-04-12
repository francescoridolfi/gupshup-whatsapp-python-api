from . import functions as func


def prefix(level):
    return "[" + func.get_time(func.get_current_timestamp()) + "] " + level + " - "


def log(text):
    print(prefix("INFO") + text)


def error(text):
    print(prefix("ERROR") + text)


def warn(text):
    print(prefix("WARN") + text)