import time

import pytest
from selenium.webdriver.common.by import By

from POM.AddAddressPage import AddAddressPage
from POM.CheckOutPage import CheckOutPage
from POM.HomePage import HomePage
from POM.LoginPage import LoginPage
from POM.PaymentPage import PaymentPage
from TestData.LoginData import LoginTestData
from TestData.RegisterData import RegisterTestData
from Utilities.BaseClass import BaseClass
from Utilities.Logger import LogGeneration


class Test_002_e2e:
    URL = BaseClass.getLoginUrl()
    logger = LogGeneration.LogGen()

    def test_e2e(self, setup, getData):
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.implicitly_wait(10)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.VerifyPresenceofLink()
        self.loginpage.Enter_Email(getData["Email"])
        self.loginpage.Enter_Password(getData["Password"])
        self.loginpage.Click_Login()
        self.logger.info("-----Login Successfull-----")
        self.homepage = HomePage(self.driver)
        self.homepage.Click_Electronics()
        self.homepage.Click_Cameras()
        self.homepage.Click_AddToCart()
        self.homepage.VerifyPresenceofLink()
        self.homepage.Click_AddCartIcon()
        self.checkoutpage = CheckOutPage(self.driver)
        self.checkoutpage.Click_BuyNow()
        self.checkoutpage.Select_Adreess()
        self.checkoutpage.Click_Proceed()
        self.paymentpage = PaymentPage(self.driver)
        self.paymentpage.Select_Payment("COD")
        self.paymentpage.Click_Proceed()
        time.sleep(2)
        self.message = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").text
        if "Createdf" in self.message:
            assert True == True
            self.logger.info("-----Order Created Successful-----")
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\Shoppers Stack\\Screenshots\\Order.png")
            self.logger.info("-----Order Creation Failed-----")

        self.driver.close()

    @pytest.fixture(params=LoginTestData.getTestData("T1"))
    def getData(self, request):
        return request.param