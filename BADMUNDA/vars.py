from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    API_ID = int(config("API_ID", default="123"))
    API_HASH = config("API_HASH", default=None)
    BOT_USERNAME = config("BOT_USERNAME" , default=None)
    OWNER_ID = int(config("OWNER_ID", default=6898413162))
    SUDO_USERS = config("SUDO_USERS", default="6352107773").split()
    WHITELIST_USERS = config("WHITELIST_USERS", default="6352107773").split()
    
    GENIUS_API_TOKEN = config("GENIUS_API",default=None)
    AuDD_API = config("AuDD_API",default=None)
    RMBG_API = config("RMBG_API",default=None)
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="BrokenroboDB")
    BDB_URI = config("BDB_URI",default=None)
    NO_LOAD = config("NO_LOAD", default="").split()
    DEV_USERS = config("DEV", default="6352107773").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="ll_BAD_GROUP_ll")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="PBX_PERMOT")
    WORKERS = int(config("WORKERS", default=16))
    TIME_ZONE = config("TIME_ZONE",default='Asia/Kolkata')


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN ="7177274563:AAFyV9BtGWhhhEkVNOeaxlu_PEZW0KxWebU"
    API_ID = 27383453
    API_HASH ="834fd6015b50b781e0f8a41876ca95c8"
    OWNER_ID =6898413162
    BOT_USERNAME = "Group_manegment_bad_bot"
    BOT_ID = 7177274563
    BOT_NAME ="grup"
    owner_username ="II_BAD_BABY_II"
    MESSAGE_DUMP =-1002093247039
    DEV_USERS = []
    DEVS_USER = 6352107773
    SUDO_USERS = 6352107773
    SUDO_USERS = []
    WHITELIST_USERS = 6352107773
    DB_URI ="mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
    DB_NAME ="BrokenroboDB"
    NO_LOAD = []
    GENIUS_API_TOKEN ="jsjnsms"
    AuDD_API = "None"
    RMBG_API ="jsnnem"
    PREFIX_HANDLER = ["!", "/","$"]
    SUPPORT_GROUP ="ll_BAD_MUNDA_ll"
    SUPPORT_CHANNEL ="PBX_PERMOT"
    VERSION = "VERSION"
    TIME_ZONE = 'Asia/Kolkata'
    BDB_URI ="mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net/"
    WORKERS = 8
    
