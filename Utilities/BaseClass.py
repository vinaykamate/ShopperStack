from lib2to3.pgen2 import driver
import pytest
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

config = configparser.RawConfigParser()
config.read("C:\\Users\\HP\\PycharmProjects\\Shoppers Stack\\Configuration\\config.ini")

class BaseClass:

    def __init__(self):
        self.driver = driver

    @staticmethod
    def getRegisterUrl():
        url = config.get('common info', 'RegisterURL')
        return url

    @staticmethod
    def getLoginUrl():
        url = config.get("common info", "LoginURL")
        return url