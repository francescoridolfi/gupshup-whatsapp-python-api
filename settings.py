from pathlib import Path
import os

# DIR

BASE_DIR = Path(__file__).resolve(strict=True).parent

# API

API_INFO = {
    "BOT_NAME": "xxxx",
    "KEY": "XXXXXXXXXXXXX",
    "NUMBER": "1234567890"

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
