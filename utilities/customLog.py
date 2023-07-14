import logging


class logGen():

    @staticmethod
    def loggen():
        logger = logging.getLogger("Test Login")
        fileHandler = logging.FileHandler('.//Logs//automation.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger