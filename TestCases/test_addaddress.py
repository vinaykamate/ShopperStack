import time
import pytest
from selenium.webdriver.common.by import By

from POM.AddAddressPage import AddAddressPage
from POM.LoginPage import LoginPage
from TestData.LoginData import LoginTestData
from Utilities.BaseClass import BaseClass
from Utilities.Logger import LogGeneration


class Test_003_AddAdressPage:
    URL = BaseClass.getLoginUrl()
    logger = LogGeneration.LogGen()

    def test_addaddress(self, setup, getData):
        self.driver = setup
        self.driver.get(self.URL)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.VerifyPresenceofLink()
        self.loginpage.Enter_Email(getData["Email"])
        self.loginpage.Enter_Password(getData["Password"])
        self.loginpage.Click_Login()
        self.logger.info("-----Login Successfull-----")
        self.addaddresspage = AddAddressPage(self.driver)
        self.addaddresspage.Click_ProfileIcon()
        self.addaddresspage.Click_MyProfile()
        self.addaddresspage.Click_MyAddress()
        self.addaddresspage.Click_AddAddress()
        self.addaddresspage.Select_AddressType()
        self.addaddresspage.Enter_Name("vinayak kamati")
        self.addaddresspage.Enter_HouseNo("537")
        self.addaddresspage.Enter_StreetInfo("Banshankari 1stage,Srinagar,Benagaluru")
        self.addaddresspage.Enter_LandMark("Near S V Tiffin")
        self.addaddresspage.Select_Country("India")
        self.addaddresspage.Select_State("Karnataka")
        self.addaddresspage.Select_City("Bengaluru")
        self.addaddresspage.Enter_PinCode("560010")
        self.addaddresspage.Enter_PhoneNumber("8951891001")
        self.addaddresspage.Click_AddAdress1()
        time.sleep(2)
        self.message = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]").text
        if "successfully added" in self.message:
            assert True == True
            self.logger.info("-----Addresss Successfully Added-----")
        else:
            self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\Shoppers Stack\\Screenshots\\Address.png")
            self.logger.info("-----Add Address Failed-----")

        self.driver.close()


    @pytest.fixture(params=LoginTestData.getTestData("T1"))
    def getData(self, request):
        return request.param