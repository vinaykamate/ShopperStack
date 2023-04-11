import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddAddressPage:
    link_profileicon_xpath = "//div[@class='MuiAvatar-root MuiAvatar-circular MuiAvatar-colorDefault css-bjoz8z']"
    link_myprofile_xpath = "//li[normalize-space()='My Profile']"
    link_myaddress_xpath = "//div[normalize-space()='My Addresses']"
    button_addaddress_xpath = "//button[normalize-space()='Add Address']"
    # link_newaddress_xpath = "//span[contains(.,'Add New Address')]"
    radiobtn_addresstype_xpath = "//input[@id='Home']"
    textbox_name_xpath = "//input[@id='Name']"
    textbox_houseno_xpath = "//input[@id='House/Office Info']"
    textbox_streetinfo_xpath = "//input[@id='Street Info']"
    textbox_landmark_xpath = "//input[@id='Landmark']"
    dropdown_country_xpath = "//select[@id='Country']"
    dropdown_state_xpath = "//select[@id='State']"
    dropdown_city_xpath = "//select[@id='City']"
    textbox_pincode_xpath = "//input[@id='Pincode']"
    textbox_phonenumber_xpath = "//input[@id='Phone Number']"
    button_addadress1_xpath = "//button[@id='addAddress']"

    def __init__(self, driver):
        self.driver = driver

    def Click_ProfileIcon(self):
        self.driver.find_element(By.XPATH, self.link_profileicon_xpath).click()

    def Click_MyProfile(self):
        time.sleep(2)
        self.myprofile = self.driver.find_element(By.XPATH, self.link_myprofile_xpath).click()

    def Click_MyAddress(self):
        self.driver.find_element(By.XPATH, self.link_myaddress_xpath).click()

    def Click_AddAddress(self):
        self.driver.find_element(By.XPATH, self.button_addaddress_xpath).click()

    # def Click_NewAddress(self):
    #     self.driver.find_element(By.XPATH, self.link_newaddress_xpath).click()

    def Select_AddressType(self):
        self.driver.find_element(By.XPATH, self.radiobtn_addresstype_xpath).click()

    def Enter_Name(self, Name):
        self.driver.find_element(By.XPATH, self.textbox_name_xpath).send_keys(Name)

    def Enter_HouseNo(self, HouseNo):
        self.driver.find_element(By.XPATH, self.textbox_houseno_xpath).send_keys(HouseNo)

    def Enter_StreetInfo(self, StreetInfo):
        self.driver.find_element(By.XPATH, self.textbox_streetinfo_xpath).send_keys(StreetInfo)

    def Enter_LandMark(self, LandMark):
        self.driver.find_element(By.XPATH, self.textbox_landmark_xpath).send_keys(LandMark)

    def Select_Country(self, Country):
        self.country = Select(self.driver.find_element(By.XPATH, self.dropdown_country_xpath))
        self.country.select_by_visible_text(Country)

    def Select_State(self, State):
        self.state = Select(self.driver.find_element(By.XPATH, self.dropdown_state_xpath))
        self.state.select_by_visible_text(State)

    def Select_City(self, City):
        self.city = Select(self.driver.find_element(By.XPATH, self.dropdown_city_xpath))
        self.city.select_by_visible_text(City)

    def Enter_PinCode(self, PinCode):
        self.driver.find_element(By.XPATH, self.textbox_pincode_xpath).send_keys(PinCode)

    def Enter_PhoneNumber(self, PhoneNumber):
        self.driver.find_element(By.XPATH, self.textbox_phonenumber_xpath).send_keys(PhoneNumber)

    def Click_AddAdress1(self):
        self.driver.find_element(By.XPATH, self.button_addadress1_xpath).click()