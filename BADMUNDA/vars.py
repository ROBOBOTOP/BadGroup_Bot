from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="27383453"))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=6898413162))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP",default="-1002093247039"))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="6898413162",
        ).split(None)
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="6898413162",
        ).split(None)
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="6898413162",
        ).split(None)
    ]
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="BrokenDB")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="PBX_CHAT")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="PBX_PERMOT")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')
    BOT_ID ="7394970820"
    BOT_NAME = "hsj"
    owner_username = "II_BAD_BABY_II"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "7177274563:AAFyV9BtGWhhhEkVNOeaxlu_PEZW0KxWebU"
    API_ID = 27383453
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"
    OWNER_ID = 6898413162
    BOT_USERNAME ="Group_manegment_bad_bot"
    MESSAGE_DUMP = -1002093247039  # Your Private Group ID for logs
    DEV_USERS = [6898413162]
    SUDO_USERS = [6898413162]
    WHITELIST_USERS = [6898413162]
    DB_URI = "mongodb+srv://Badmunda_13:badmunda50@cluster0.9oyzqux.mongodb.net/?retryWrites=true&w=majority"
    DB_NAME = "BrokenDB"
    NO_LOAD = [6898413162]
    GENIUS_API_TOKEN = "JSJSJ"
    RMBG_API = "HSJJ"
    AuDD_API = "badhi"
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP = "PBX_CHAT"
    SUPPORT_CHANNEL = "PBX_PERMOT"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI = "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
    WORKERS = 8
