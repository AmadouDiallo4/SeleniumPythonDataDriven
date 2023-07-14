import configparser
import os.path

config = configparser.RawConfigParser()
ROOT_DIR = "Configurations"
config_path = os.path.join(ROOT_DIR, "config.ini")
config_read = config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common data", "BASE_URL")
        return url

    @staticmethod
    def getUsername():
        username = config.get("common data", "username")
        return username


    @staticmethod
    def getPassword():
        password = config.get("common data", "password")
        return password