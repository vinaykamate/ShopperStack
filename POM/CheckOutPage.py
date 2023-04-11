from selenium.webdriver.common.by import By


class CheckOutPage:
    text_canoncamera_xpath = "//p[contains(text(),'Canon EOS 90D Digital SLR Camera with 18-135mm USM')]"
    button_buynow_xpath = "//span[normalize-space()='Buy Now']"
    radiobtn_address_xpath = "/html[1]/body[1]/div[1]/div[4]/div[2]/div[1]/input[1]"
    button_proceed_xpath = "//button[contains(text(),'Proceed')]"

    def __init__(self, driver):
        self.driver = driver

    def Click_BuyNow(self):
        self.driver.find_element(By.XPATH, self.button_buynow_xpath).click()

    def Select_Adreess(self):
        self.driver.find_element(By.XPATH, self.radiobtn_address_xpath).click()

    def Click_Proceed(self):
        self.driver.find_element(By.XPATH, self.button_proceed_xpath).click()


    def Click_Proceed2(self):
        self.driver.find_element(By.XPATH, self.button_proceed2_xpath).click()

