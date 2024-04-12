from pathlib import Path
import os

# DIR

BASE_DIR = Path(__file__).resolve(strict=True).parent

# API

API_INFO = {
    "BOT_NAME": "pankapuzza",
    "KEY": "0d255125d481452dc51c87c03dc45c51",
    "NUMBER": "917834811114"

}

# CALLBACK SETTINGS

SERVER = {
    "ENABLE": True,
    "HOST": "",
    "PORT": 8000,
    "LOGS": {
        "ENABLE": True,
        "PATH": os.path.join(BASE_DIR, "logs.txt")
    }
}

# CUSTOM SCRIPTS

CUSTOM_SCRIPTS = {
    "ENABLE": True,
    "PATH": os.path.join(BASE_DIR, "scripts"),
    "SCRIPTS": ["info_frutta"]
}