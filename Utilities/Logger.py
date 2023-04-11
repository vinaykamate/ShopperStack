import logging

class LogGeneration:

    @staticmethod
    def LogGen():
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler("C:\\Users\\HP\\PycharmProjects\\Shoppers Stack\\Logs\\automation.log")
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)
        return logger
