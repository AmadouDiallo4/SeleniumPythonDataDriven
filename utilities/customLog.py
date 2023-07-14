import logging


class logGen():

    @staticmethod
    def loggen():
        # getLogger() method takes the test case name as input
        logger = logging.getLogger("Test Login")
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('.//Logs//automation.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s :%(message)s")
        # addHandler() method takes fileHandler object as parameter
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.INFO)
        return logger