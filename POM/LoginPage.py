from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    textbox_Email_cssselector = "#Email"
    textbox_Password_cssselector = "#Password"
    button_Login_xpath = "(//span[@class='MuiButton-label'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def VerifyPresenceofLink(self):
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#Email")))

    def Enter_Email(self, Email):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_Email_cssselector).send_keys(Email)

    def Enter_Password(self, Password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_Password_cssselector).send_keys(Password)

    def Click_Login(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()