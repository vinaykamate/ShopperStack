import time
import pytest
from selenium.webdriver.common.by import By

from POM.Register_Page import RegisterPage
from TestData.RegisterData import RegisterTestData
from Utilities.BaseClass import BaseClass
from Utilities.Logger import LogGeneration


class Test_001_Register:
    URL = BaseClass.getRegisterUrl()
    logger = LogGeneration.LogGen()

    def test_register(self, setup, getData):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.registerpage = RegisterPage(self.driver)
        self.registerpage.VerifyPresenceofLink()
        self.registerpage.Enter_FirstName(getData["FirstName"])
        self.registerpage.Enter_LastName(getData["LastName"])
        self.registerpage.Select_Gender(getData["Gender"])
        self.registerpage.Enter_PhoneNumber(getData["PhoneNumber"])
        self.registerpage.Enter_Email(getData["Email"])
        self.registerpage.Enter_Password(getData["Password"])
        self.registerpage.Enter_ConfirmPassword(getData["ConfirmPassword"])
        self.registerpage.Select_Terms_and_condition()
        self.registerpage.Click_Register()
        time.sleep(2)
        self.message = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").text
        print(self.message)
        if "successfully Registered" in self.message:
            assert True == True
            self.logger.info("-----User Successfully Registered-----")
        elif "Given Email ID or Phone number already used" in self.message:
            self.logger.info("-----Given User Email ID or Phone number already used-----")
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\Shoppers Stack\\Screenshots\\Register.png")
            self.logger.info("-----User Registration Failed-----")

        self.driver.close()

    @pytest.fixture(params=RegisterTestData.getTestData("T2"))
    def getData(self, request):
        return request.param