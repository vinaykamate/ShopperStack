from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class RegisterPage:

    textbox_firstname_xpath = "//input[@id='First Name']"
    textbox_lastname_xpath = "//input[@id='Last Name']"
    radiobtn_gendermale_cssselector = "#Male"
    radiobtn_genderfemale_cssselector = "#Female"
    radiobtn_genderother_cssselector = "#Other"
    textbox_phonenumber_xpath = "//input[@id='Phone Number']"
    textbox_email_xpath = "//input[@id='Email Address']"
    textbox_password_xpath = "//input[@id='Password']"
    textbox_confirmpassword_xpath = "//input[@id='Confirm Password']"
    checkbox_tc_xpath = "//input[@id='Terms and Conditions']"
    button_register_cssselector = ".signup_bn5__l1dQe"

    def __init__(self, driver):
        self.driver = driver

    def VerifyPresenceofLink(self):
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='First Name']")))

    def Enter_FirstName(self, FirstName):
        self.driver.find_element(By.XPATH, self.textbox_firstname_xpath).send_keys(FirstName)

    def Enter_LastName(self, LastName):
        self.driver.find_element(By.XPATH, self.textbox_lastname_xpath).send_keys(LastName)

    def Select_Gender(self, Gender):
        if Gender == "Male":
            self.driver.find_element(By.CSS_SELECTOR, self.radiobtn_gendermale_cssselector).click()
        elif Gender == "Female":
            self.driver.find_element(By.CSS_SELECTOR, self.radiobtn_genderfemale_cssselector).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.radiobtn_genderother_cssselector).click()

    def Enter_PhoneNumber(self, PhoneNumber):
        self.driver.find_element(By.XPATH, self.textbox_phonenumber_xpath).send_keys(PhoneNumber)

    def Enter_Email(self, Email):
        self.driver.find_element(By.XPATH, self.textbox_email_xpath).send_keys(Email)

    def Enter_Password(self, Password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(Password)

    def Enter_ConfirmPassword(self, ConfirmPassword):
        self.driver.find_element(By.XPATH, self.textbox_confirmpassword_xpath).send_keys(ConfirmPassword)

    def Select_Terms_and_condition(self):
        self.driver.find_element(By.XPATH, self.checkbox_tc_xpath).click()

    def Click_Register(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_register_cssselector).click()
